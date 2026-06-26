# Phytochemical Compound Management System

A command-line object-oriented Python application for managing, evaluating, and ranking phytochemical compounds based on drug-likeness criteria. Built as part of a Machine Learning for Drug Discovery curriculum.

**Author:** Ogerovor Joy Ben  
**Language:** Python 
**Paradigm:** Object-Oriented Programming

---

## Features

- Add phytochemical compounds with full molecular property profiles
- Categorize compounds by class (Flavonoid, Alkaloid, Terpenoid, Phenolic Acid)
- Search compounds by name or source plant
- Evaluate drug-likeness using Lipinski's Rule of Five
- Rank compounds by drug-likeness score, molecular weight, or LogP
- Export shortlisted compounds to CSV or TXT

---

## OOP Concepts Demonstrated

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation (private attributes with `@property` getters and setters)
- Inheritance (subclass hierarchy from base `Compound` class)
- Polymorphism (overridden `__str__` across subclasses)
- Composition (Plant and CompoundDatabase holding Compound objects)
- Magic Methods (`__str__`)
- Class Methods and Instance Methods

---

## Project Structure

```
Compound (base class)
├── Flavonoid
├── Alkaloid
├── Terpenoid
└── PhenolicAcid

Plant
CompoundDatabase
DrugLikenessEvaluator
CompoundRanker
DataExporter
---

## Classes Overview

### `Compound`
Base class storing molecular properties: name, molecular weight, LogP, HBA, HBD, SMILES, and source plant. Includes validated setters for all numeric attributes.

### `Flavonoid`, `Alkaloid`, `Terpenoid`, `PhenolicAcid`
Subclasses of `Compound`, each with a specialized method reflecting the biological or chemical significance of that compound category.

### `Plant`
Stores a collection of Compound objects associated with a given plant. Supports adding, displaying, and counting compounds.

### `CompoundDatabase`
Dictionary-based database for storing and retrieving all compounds. Supports add, remove, search by name, search by plant, and view all.

### `DrugLikenessEvaluator`
Evaluates compounds against Lipinski's Rule of Five:
- Molecular Weight ≤ 500
- LogP ≤ 5
- HBA ≤ 10
- HBD ≤ 5

Generates a score (0–4) and labels compounds as Excellent, Moderate, or Poor Candidates.

### `CompoundRanker`
Sorts a list of compounds by drug-likeness score (descending), molecular weight (ascending), or LogP (ascending).

### `DataExporter`
Exports compound data to `.csv` (with drug-likeness labels) or `.txt` format.

---

## How to Run

```bash
python3 "Phytochemical_compound_management_system.py"
```

### Menu Options

```
=== Phytochemical Compound Management System ===
1. Add Compound
2. Search Compound
3. Evaluate Drug-Likeness
4. Rank Compounds
5. Export Results
6. Exit
```

### Exporting Files
When prompted for a filename, enter the full path:
```
/Users/yourusername/Desktop/results.csv
```

---

## Requirements

- Python 3.x
- No external libraries required (uses built-in `csv` module only)

---

## License

This project is for educational purposes as part of a Machine Learning for Drug Discovery training track.
