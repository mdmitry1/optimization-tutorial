#!/usr/bin/env python3.12

# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import pandas as pd
import numpy as np
import random
from hashlib import sha256
from deap import base, creator, tools, algorithms
import os, matplotlib; matplotlib.use("TkAgg" if os.environ.get("DISPLAY") else "Agg")
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from sys import argv
from math import inf

products_data = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D'],
    'cost': [10, 15, 20, 12],
    'profit': [30, 45, 50, 35],
    'weight': [2, 3, 4, 2.5],
    'min_quantity': [5, 3, 2, 4],
    'max_quantity': [20, 25, 15, 30]
})



# Resources data: available capacity
resources_data = pd.DataFrame({
    'resource': ['labor_hours', 'machine_hours', 'storage_space'],
    'capacity': [100, 80, 50]
})

# Product-Resource requirements
requirements_data = pd.DataFrame({
    'product': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'resource': ['labor_hours', 'machine_hours', 'storage_space'] * 4,
    'requirement': [2, 1, 0.5, 3, 2, 0.8, 4, 2.5, 1, 2.5, 1.5, 0.6]
})

# Create requirement dictionary for quick lookup
req_dict = {}
for _, row in requirements_data.iterrows():
    req_dict[(row['product'], row['resource'])] = row['requirement']

# ============================================================================
# CUSTOM CONSTRAINT FUNCTIONS (Python functions as requested)
# ============================================================================

def check_resource_constraints(individual):
    """Check if resource capacity constraints are satisfied"""
    for idx, resource in enumerate(resources_data['resource']):
        capacity = resources_data.iloc[idx]['capacity']
        used = 0
        for i, product in enumerate(products_data['product']):
            qty = individual[i]
            used += req_dict.get((product, resource), 0) * qty
        
        if used > capacity:
            return False
    return True

def check_min_quantity(individual):
    """Check minimum quantity constraints"""
    for i, row in products_data.iterrows():
        if individual[i] < row['min_quantity']:
            return False
    return True

def check_weight_limit(individual):
    """Complex constraint: Total weight cannot exceed 60 units"""
    total_weight = sum(products_data.iloc[i]['weight'] * individual[i] 
                      for i in range(len(individual)))
    return total_weight <= 60

def check_ratio_constraint(individual):
    """Product B must be at least 30% of Product A"""
    product_a_qty = individual[0]  # Product A
    product_b_qty = individual[1]  # Product B
    if product_a_qty > 0:
        return product_b_qty >= 0.3 * product_a_qty
    return True

def check_all_constraints(individual):
    """Apply all constraint functions"""
    return (check_resource_constraints(individual) and 
            check_min_quantity(individual) and 
            check_weight_limit(individual) and 
            check_ratio_constraint(individual))

# ============================================================================
# OBJECTIVE FUNCTION
# ============================================================================

def evaluate_profit(individual):
    """
    Objective function: Maximize profit
    Returns tuple for DEAP (must return tuple even for single objective)
    Applies penalty for constraint violations
    """
    # Calculate base profit
    total_profit = sum(products_data.iloc[i]['profit'] * individual[i] 
                      for i in range(len(individual)))
    
    # Apply penalty if constraints are violated
    if not check_all_constraints(individual):
        # Heavy penalty for constraint violation
        penalty = 10000
        
        # Calculate specific penalties for better guidance
        # Resource constraint penalties
        for idx, resource in enumerate(resources_data['resource']):
            capacity = resources_data.iloc[idx]['capacity']
            used = sum(req_dict.get((products_data.iloc[i]['product'], resource), 0) * individual[i]
                      for i in range(len(individual)))
            if used > capacity:
                penalty += (used - capacity) * 100
        
        # Weight constraint penalty
        total_weight = sum(products_data.iloc[i]['weight'] * individual[i] 
                          for i in range(len(individual)))
        if total_weight > 60:
            penalty += (total_weight - 60) * 50
        
        total_profit -= penalty
    
    return (total_profit,)  # Must return tuple

# ============================================================================
# DEAP SETUP
# ============================================================================

# Create fitness and individual classes
# FitnessMax means we're maximizing (use FitnessMin for minimization)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Define how to create genes (product quantities)
# Each gene is a float between min and max quantity for each product
def create_quantity(product_idx):
    min_qty = products_data.iloc[product_idx]['min_quantity']
    max_qty = products_data.iloc[product_idx]['max_quantity']
    return random.uniform(min_qty, max_qty)

# Register gene creation for each product
for i in range(len(products_data)):
    toolbox.register(f"attr_product_{i}", create_quantity, i)

# Create individual (chromosome) - list of quantities for all products
def create_individual():
    return creator.Individual([getattr(toolbox, f"attr_product_{i}")() 
                              for i in range(len(products_data))])

toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register genetic operators
toolbox.register("evaluate", evaluate_profit)
toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Crossover
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=2, indpb=0.2)  # Mutation
toolbox.register("select", tools.selTournament, tournsize=3)  # Selection

# Repair function to ensure quantities stay within bounds
def repair_individual(individual):
    for i in range(len(individual)):
        min_qty = products_data.iloc[i]['min_quantity']
        max_qty = products_data.iloc[i]['max_quantity']
        individual[i] = max(min_qty, min(max_qty, individual[i]))
    return individual

# ============================================================================
# RUN GENETIC ALGORITHM
# ============================================================================

def run_ga():
    random.seed(42)
    np.random.seed(42)
    
    # GA Parameters
    POPULATION_SIZE = 100
    GENERATIONS = 50
    CROSSOVER_PROB = 0.8
    MUTATION_PROB = 0.2
    
    print(f"\nGenetic Algorithm Parameters:")
    print(f"  Population Size: {POPULATION_SIZE}")
    print(f"  Generations: {GENERATIONS}")
    print(f"  Crossover Probability: {CROSSOVER_PROB}")
    print(f"  Mutation Probability: {MUTATION_PROB}")
    print("\nRunning optimization...\n")
    
    # Create initial population
    population = toolbox.population(n=POPULATION_SIZE)
    
    # Statistics tracking
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    # Hall of Fame - keeps track of best individuals
    hof = tools.HallOfFame(1)
    
    # Run the algorithm
    population, logbook = algorithms.eaSimple(
        population, toolbox,
        cxpb=CROSSOVER_PROB,
        mutpb=MUTATION_PROB,
        ngen=GENERATIONS,
        stats=stats,
        halloffame=hof,
        verbose=True
    )
    
    return population, logbook, hof

# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_results(best_individual, logbook, rootpath=".", timeout=inf):
    """
    Produce a 2x2 matplotlib figure summarising GA results:
      [0,0] Evolution curves  – max & avg fitness over generations
      [0,1] Optimal quantities – horizontal bar chart per product
      [1,0] Resource utilisation – grouped bar (used vs capacity)
      [1,1] Profit breakdown – pie chart of per-product profit contribution
    Saves to <rootpath>/ga_results.png (Agg backend, no display required).
    """
    gen          = logbook.select("gen")
    max_fitness  = logbook.select("max")
    avg_fitness  = logbook.select("avg")

    quantities   = [round(q, 2) for q in best_individual]
    profits      = [round(q * products_data.iloc[i]['profit'], 2)
                    for i, q in enumerate(quantities)]
    product_names = list(products_data['product'])

    resources    = list(resources_data['resource'])
    capacities   = list(resources_data['capacity'])
    used_list    = [
        sum(req_dict.get((products_data.iloc[i]['product'], r), 0) * quantities[i]
            for i in range(len(quantities)))
        for r in resources
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("GA Optimisation Results", fontsize=14, fontweight='bold')
    colors = ['#185FA5', '#1D9E75', '#BA7517', '#A32D2D']

    # ── [0,0] Evolution curves ────────────────────────────────────────────────
    ax = axes[0, 0]
    ax.plot(gen, max_fitness, color='#185FA5', linewidth=2, label='Max fitness')
    ax.plot(gen, avg_fitness, color='#1D9E75', linewidth=2,
            linestyle='--', label='Avg fitness')
    ax.set_title("Fitness over generations", fontsize=11)
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness ($)")
    ax.legend(framealpha=0.3)
    ax.grid(axis='y', linewidth=0.4, alpha=0.5)
    ax.spines[['top', 'right']].set_visible(False)

    # ── [0,1] Optimal quantities ──────────────────────────────────────────────
    ax = axes[0, 1]
    bars = ax.barh(product_names, quantities, color=colors, height=0.55)
    for bar, qty in zip(bars, quantities):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f'{qty:.1f}', va='center', fontsize=10)
    ax.set_title("Optimal production quantities", fontsize=11)
    ax.set_xlabel("Quantity")
    ax.set_xlim(0, max(quantities) * 1.25)
    ax.spines[['top', 'right']].set_visible(False)
    # overlay min/max range markers
    for i, name in enumerate(product_names):
        mn = products_data.iloc[i]['min_quantity']
        mx = products_data.iloc[i]['max_quantity']
        ax.plot([mn, mx], [i, i], color='#888', linewidth=6, alpha=0.15,
                solid_capstyle='round')

    # ── [1,0] Resource utilisation ────────────────────────────────────────────
    ax = axes[1, 0]
    x   = np.arange(len(resources))
    w   = 0.38
    b1  = ax.bar(x - w/2, used_list,   width=w, color='#185FA5', label='Used')
    b2  = ax.bar(x + w/2, capacities,  width=w, color='#D3D1C7', label='Capacity')
    for bar, val in zip(b1, used_list):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f'{val:.1f}', ha='center', fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels([r.replace('_', '\n') for r in resources], fontsize=9)
    ax.set_title("Resource utilisation", fontsize=11)
    ax.set_ylabel("Units")
    ax.legend(framealpha=0.3)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', linewidth=0.4, alpha=0.5)

    # ── [1,1] Profit breakdown ────────────────────────────────────────────────
    ax = axes[1, 1]
    wedge_props = {'linewidth': 0.8, 'edgecolor': 'white'}
    wedges, texts, autotexts = ax.pie(
        profits, labels=product_names, colors=colors,
        autopct='%1.1f%%', startangle=90,
        wedgeprops=wedge_props, pctdistance=0.78
    )
    for at in autotexts:
        at.set_fontsize(9)
    total = sum(profits)
    ax.set_title(f"Profit breakdown  (total: ${total:.0f})", fontsize=11)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = f"{rootpath}/ga_results.png"
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    if not inf == timeout:
        timer = fig.canvas.new_timer(interval=timeout, callbacks=[(plt.close, [], {})])
        timer.start()
    plt.show()
    plt.close(fig)
    print(f"\nPlot saved → {out_path}")
    return out_path


def main(rootpath: str = ".", timeout: float=5000) -> int:
    # Create sample CSV files for demonstration
    # In practice, you'd read these from actual CSV files
    
    # Products data: cost, profit, weight per unit
    
    # Save to CSV (optional - for demonstration)
    products_data.to_csv(rootpath + '/products_ga.csv', index=False)
    resources_data.to_csv(rootpath + '/resources_ga.csv', index=False)
    requirements_data.to_csv(rootpath + '/requirements_ga.csv', index=False)
    
    print("=" * 70)
    print("GENETIC ALGORITHM OPTIMIZATION: Production Planning with DEAP")
    print("=" * 70)
    
    
    
    # Run the optimization
    population, logbook, hof = run_ga()
    
    # ============================================================================
    # DISPLAY RESULTS
    # ============================================================================
    
    print("\n" + "=" * 70)
    print("OPTIMIZATION RESULTS")
    print("=" * 70)
    
    best_individual = hof[0]
    best_individual = repair_individual(best_individual)
    
    print(f"\nBest Profit: ${evaluate_profit(best_individual)[0]:.2f}")
    print(f"Constraints Satisfied: {check_all_constraints(best_individual)}")
    
    print("\n" + "-" * 70)
    print("Optimal Production Quantities:")
    print("-" * 70)
    results_df = pd.DataFrame({
        'Product': products_data['product'],
        'Quantity': [round(qty, 2) for qty in best_individual],
        'Profit_per_Unit': products_data['profit'],
        'Total_Profit': [round(qty * products_data.iloc[i]['profit'], 2) 
                         for i, qty in enumerate(best_individual)]
    })
    print(results_df.to_string(index=False))
    
    print("\n" + "-" * 70)
    print("Resource Utilization:")
    print("-" * 70)
    resource_usage = []
    for idx, resource in enumerate(resources_data['resource']):
        capacity = resources_data.iloc[idx]['capacity']
        used = sum(req_dict.get((products_data.iloc[i]['product'], resource), 0) * best_individual[i]
                  for i in range(len(best_individual)))
        resource_usage.append({
            'Resource': resource,
            'Used': round(used, 2),
            'Capacity': capacity,
            'Utilization_%': round(used / capacity * 100, 2)
        })
    resource_df = pd.DataFrame(resource_usage)
    print(resource_df.to_string(index=False))
    
    print("\n" + "-" * 70)
    print("Constraint Verification:")
    print("-" * 70)
    total_weight = sum(products_data.iloc[i]['weight'] * best_individual[i] 
                      for i in range(len(best_individual)))
    print(f"Total Weight: {total_weight:.2f} (limit: 60)")
    ratio = best_individual[1] / max(best_individual[0], 0.001)
    print(f"Product B / Product A ratio: {ratio:.2%} (min: 30%)")
    print(f"All resource constraints: {'✓ Satisfied' if check_resource_constraints(best_individual) else '✗ Violated'}")
    print(f"Minimum quantities: {'✓ Satisfied' if check_min_quantity(best_individual) else '✗ Violated'}")
    
    print("\n" + "-" * 70)
    print("Evolution Statistics:")
    print("-" * 70)
    gen = logbook.select("gen")
    max_fitness = logbook.select("max")
    avg_fitness = logbook.select("avg")
    
    print(f"Generation 0 - Max Fitness: ${max_fitness[0]:.2f}, Avg: ${avg_fitness[0]:.2f}")
    print(f"Generation {len(gen)//2} - Max Fitness: ${max_fitness[len(gen)//2]:.2f}, Avg: ${avg_fitness[len(gen)//2]:.2f}")
    last_generation = (f"Generation {len(gen)-1} - Max Fitness: ${max_fitness[-1]:.2f}, Avg: ${avg_fitness[-1]:.2f}")
    print(last_generation)
    
    print("\n" + "=" * 70)
    print("To use with your own CSV files:")
    print("  products_data = pd.read_csv('your_products.csv')")
    print("  resources_data = pd.read_csv('your_resources.csv')")
    print("  requirements_data = pd.read_csv('your_requirements.csv')")
    print("=" * 70)

    # Produce and save visualisation
    plot_results(best_individual, logbook, rootpath,timeout)

    return sha256(last_generation.encode()).hexdigest()

if __name__ == "__main__":
    rootpath = "." if len(argv) < 2 else argv[1]
    timeout = inf if len(argv) < 3 else argv[2]
    print(main(rootpath,timeout))
