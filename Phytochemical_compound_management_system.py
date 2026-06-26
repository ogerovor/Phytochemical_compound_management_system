# oop milestone project
#To create a phytochemical compound management system
import csv

class Compound:
    def __init__(self,name,mol_weight,logp,hba,hbd,smiles,source_plant):
        self._name = name
        self._mol_weight = mol_weight
        self._logp = logp
        self._hba = hba
        self._hbd = hbd
        self._smiles = smiles
        self._source_plant = source_plant

    @property
    def mol_weight(self):
        return self._mol_weight
    
    @property
    def logp(self):
        return self._logp
    
    @property
    def hba(self):
        return self._hba
    
    @property
    def hbd(self):
        return self._hbd
    
    @property
    def smiles(self):
        return self._smiles
    
    @property
    def name(self):
        return self._name
    
    @property
    def source_plant(self):
        return self._source_plant
    
    @mol_weight.setter
    def mol_weight(self, value):
        if value <= 0:
            raise ValueError("Molecular weight must be greater than zero")
        self._mol_weight = value

    @logp.setter
    def logp(self, value):
        if value <= -10:
            raise ValueError("LogP must be positive")
        elif value >= 10:
            raise ValueError("LogP must be less than 10")
        self._logp = value

    @hba.setter
    def hba(self, value):
        if value < 0:
            raise ValueError("Hydrogen bond acceptor must be greater than zero")
        self._hba = value

    @hbd.setter
    def hbd(self, value):
        if value < 0:
            raise ValueError("Hydrogen bond donor must be greater than zero")
        self._hbd = value

    @smiles.setter
    def smiles(self, value):
        if value == "":
            raise ValueError("smiles cannot be empty")
        self._smiles = value

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self._name = value

    def display_profile(self):
        print(f"{self.name}|MW={self.mol_weight}|LogP={self.logp}|HBA={self.hba}|HBD={self.hbd}|smiles:{self.smiles}|Plant of origin:{self.source_plant}")


    def update_property(self,attr_name,value):
        if attr_name == "mol_weight":
            self.mol_weight = value
        elif attr_name == "hba":
            self.hba = value
        elif attr_name == "logp":
            self.logp = value
        elif attr_name == "name":
            self.name = value
        elif attr_name == "hbd":
            self.hbd = value
        else:
            print(f"{attr_name} is unknown")

    def __str__(self):
        return f"{self.name}|MW={self.mol_weight}|LogP={self.logp}|HBA={self.hba}|HBD={self.hbd}|"

class Flavonoid(Compound):
    def __init__(self, name, mol_weight, logp, hba, hbd, smiles, source_plant):
        super().__init__(name, mol_weight, logp, hba, hbd, smiles, source_plant)

    def antioxidant_profile(self):
        return f"Flavonoids are potent antioxidants that neutralize free radicals by donating hydrogen atoms.Commonly linked to anti-inflammatory activity"

    def __str__(self):
        return f"[Flavonoid] {super().__str__()}" 
    
class Alkaloid(Compound):
    def __init__(self, name, mol_weight, logp, hba, hbd, smiles, source_plant):
        super().__init__(name, mol_weight, logp, hba, hbd, smiles, source_plant)
    
    def potency_warning(self):
        return f"Alkaloids contain nitrogen heterocycles and are highly bioactive at low doses.Requires careful dose calibration in in vivo studies due to potential cytotoxicity."
    
    def __str__(self):
        return f"[Alkaloid] {super().__str__()}" 
    
class Terpenoid(Compound):
    def __init__(self, name, mol_weight, logp, hba, hbd, smiles, source_plant):
        super().__init__(name, mol_weight, logp, hba, hbd, smiles, source_plant)

    def structural_note(self):
        return f"Terpenoids are built from isoprene units and exhibit diverse bioactivity including anti-inflammatory, antimicrobial, and anticancer properties depending on their carbon skeleton"
    
    def __str__(self):
        return f"[Terpenoid] {super().__str__()}" 
    
class Phenolic_Acid(Compound):
    def __init__(self, name, mol_weight, logp, hba, hbd, smiles, source_plant):
        super().__init__(name, mol_weight, logp, hba, hbd, smiles, source_plant)
    
    def oxidative_stress_relevance(self):
        return f"Phenolic acids are strong free radical scavengers due to their hydroxylated aromatic rings.Highly relevant in oxitative stress and PCOS-related inflammation research."
    
    def __str__(self):
        return f"[Phenolic acid] {super().__str__()}" 
    
class Plant:
    def __init__(self,name):
        self.name = name
        self.compounds = []

    def add_compound(self,compound):
        self.compounds.append(compound)

    def display_compounds(self):
        for compounds in self.compounds:
            print(compounds.__str__())

    def count_compounds(self):
        return len(self.compounds)
    
class CompoundDatabase:
    def __init__(self):
        self.database = {}

    def add_compound(self,compound):
        self.database[compound.name] = compound

    def remove_compound(self,name):
        if name in self.database:
            del self.database[name]
        else:
            print(f"Compound not found")

    def search_by_name(self,name):
        if name in self.database:
            return self.database[name]
        else:
            print(f'{name} does not exist')

    def search_by_plant(self,plant_name):
        result = []
        for compound in self.database.values():
            if compound.source_plant == plant_name:
                result.append(compound)
        return result
    

    def view_all(self):
        for compound in self.database.values():
            print(compound.__str__())

class DrugLikenessEvaluator:
    def __init__(self):
        pass

    def check_lipinski(self,compound):
        result = {}
        result["MW is less than 500"]= compound.mol_weight <= 500
        result["LogP is less than 5"]= compound.logp <= 5
        result["HBA is less than 10"]= compound.hba <= 10
        result["HBD is less than 5"]= compound.hbd <=5
        return result
    
    def generate_score(self,compound):
        result = self.check_lipinski(compound)
        return sum(result.values())
    
    def label_compound(self,compound):
        if self.generate_score(compound) == 4:
            return("Excellent Candidate")
        elif self.generate_score(compound) == 2 or self.generate_score(compound) ==3:
            return("Moderate Candidate")
        elif self.generate_score(compound) == 0 or self.generate_score(compound)==1:
            return("Poor Candidate")
        else:
            return("Invalid Candidate")
class CompoundRanker:
    def __init__(self):
        pass

    def rank_by_score(self,compound,evaluator):
        return sorted(compound,key=lambda compound:evaluator.generate_score(compound),reverse= True)
    
    def rank_by_mw(self,compound):
        return sorted(compound,key=lambda compound:compound.mol_weight)
    
    def rank_by_logp(self,compound):
        return sorted(compound,key=lambda compound:compound.logp)
    
class DataExporter:
    def __init__(self):
        pass

    def export_to_csv(self,filename,compounds,evaluator):
        with open(filename, "w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Name","MW","LogP","HBA","HBD","SMILES","Source Plant","Drug_likeness score"])
            for compound in compounds:
                writer.writerow([compound.name,compound.mol_weight,compound.logp,compound.hba,compound.hbd,compound.smiles,compound.source_plant,evaluator.label_compound(compound)])
    def export_to_txt(self,filename,compounds):
        with open(filename,"w", newline="") as file:
            for compound in compounds:
                file.write(compound.__str__()+"\n")
    
def main():
    # create all your objects
    db = CompoundDatabase()
    evaluator = DrugLikenessEvaluator()
    ranker = CompoundRanker()
    exporter = DataExporter()
    
    # preload your 10 compounds into db here
    while True:
            print("\n=== Phytochemical Compound Management System ===")
            print("1. Add Compound")
            print("2. Search Compound")
            print("3. Evaluate Drug-Likeness")
            print("4. Rank Compounds")
            print("5. Export Results")
            print("6. Exit")
            
            choice = input("Choose: ")

            if choice == "6":
                print("Goodbye")
                break
            elif choice == "1":
                print("\n1. Flavonoid  2. Alkaloid  3. Terpenoid  4. Phenolic Acid")
                type_choice = input("Select compound type: ")
        
                name = input("Enter compound name: ")
        
                while True:
                    try:
                        mol_weight = float(input("Enter molecular weight: "))
                        break
                    except ValueError:
                        print("Invalid. Enter a number e.g. 302.24")
        
                while True:
                    try:
                        logp = float(input("Enter LogP: "))
                        break
                    except ValueError:
                        print("Invalid. Enter a number")
        
                while True:
                    try:
                        hba = int(input("Enter HBA: "))
                        break
                    except ValueError:
                        print("Invalid. Enter a whole number")
        
                while True:
                    try:
                        hbd = int(input("Enter HBD: "))
                        break
                    except ValueError:
                        print("Invalid. Enter a whole number")
        
                smiles = input("Enter SMILES: ")
                source_plant = input("Enter source plant: ")
        
                compound_types = {"1": Flavonoid, "2": Alkaloid, "3": Terpenoid, "4": Phenolic_Acid}
                CompoundClass = compound_types.get(type_choice, Compound)
                compound = CompoundClass(name, mol_weight, logp, hba, hbd, smiles, source_plant)
                db.add_compound(compound)
                print(f"{name} added successfully!")

            elif choice == "2":
                print("\n1.Search by Name 2.Search by Plant")
                type_choice = input("Select how you want to search:")

                if type_choice == "1":
                    name = input("Enter compounds Name:")
                    compound = db.search_by_name(name)
                    print(compound)
                    
                elif type_choice == "2":
                    plant_name = input("Enter Plant Name:")
                    results = db.search_by_plant(plant_name)
                    for compound in results:
                        print(compound)

            elif choice == "3":
                name = input("Enter compound name: ")
                compound = db.search_by_name(name)
                print(evaluator.check_lipinski(compound))
                print(evaluator.generate_score(compound))
                print(evaluator.label_compound(compound))

            elif choice == "4":
                print("\n1.Rank by score 2. Rank by Molecular weight 3. Rank by Logp")
                type_choice = input("Select how you want to rank compounds: ")

                if type_choice == "1":
                    list_of_compound = list(db.database.values())
                    ranked = ranker.rank_by_score(list_of_compound, evaluator)
                    for compound in ranked:
                        print(compound)

                elif type_choice == "2":
                    list_of_compound = list(db.database.values())
                    ranked = ranker.rank_by_mw(list_of_compound)
                    for compound in ranked:
                        print(compound)

                elif type_choice == "3":
                    list_of_compound = list(db.database.values())
                    ranked = ranker.rank_by_logp(list_of_compound)
                    for compound in ranked:
                        print(compound)

            elif choice == "5":
                print("\n1.Export as CSV 2.Export as TxT")
                type_choice = input("Select your preferred file format:")

                filename = input("Enter Filename with full path(e.g. /Users/mac/desktop/filename.txt): ")

                if type_choice == "1":
                    compounds = list(db.database.values())
                    exporter.export_to_csv(filename,compounds,evaluator)
                    print(f'{filename} exported sucessfully!')
                    
                elif type_choice == "2":
                    compounds = list(db.database.values())
                    exporter.export_to_txt(filename,compounds)
                    print(f'{filename} exported sucessfully!')
main()