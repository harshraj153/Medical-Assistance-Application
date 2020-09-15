import sys

priCare = input("What Family Practicioner: ")
if priCare != "":
   priCareNum = input("\nPhone Number for " + priCare + ": ")

print("\n1. PPO")
print("2. HMO-Open Access")
print("3. HMO")
print("4. Kaiser Permanente")
Insurance = input("Which Health Insurance(Select Number): ")
if Insurance == "1": Insurance = "PPO"
elif Insurance == "2": Insurance = "HMO-Open Access"
elif Insurance == "3": Insurance = "HMO"
elif Insurance == "4": Insurance = "Kaiser Permanente"

if priCare == "":
   priCare = "FARRELL PEDIATRICS"
   priCareNum = "(703) 435-0808"
if Insurance == "":
   Insurance = "PPO"

f = open("HospitalData.txt","r")
f1 = f.readlines()
orig = {}
data = {}
for i in f1:
   h = i.split(" ")
   dist = h[1]
   del h[1]
   h[-1] = h[-1].strip()
   orig[float(dist)] = h
for key in sorted(orig.keys()):
   data[key] = orig[key]

fK = open("KaiserHospitals.txt","r")
fK1 = fK.readlines()
origK = {}
dataK = {}
for i in fK1:
   h = i.split(" ")
   dist = h[1]
   del h[1]
   h[-1] = h[-1].strip()
   origK[float(dist)] = h
for key in sorted(origK.keys()):
   dataK[key] = origK[key]

symp = input("\nWhat symptoms (seperate by commas): ")
symp = symp.split(",")
for i in range(len(symp)):
   symp[i] = symp[i].strip()

symToEquip = {"covid-19 symptoms":[1,3,10,11,2,7,8], "unconscience":[1,3,10,11,2,4,5,6,7,9], 
              "seizure":[1,3,10,11,2,4,5,6,7,9], "excessive blood":[1,3,10,11,2,4,5,6,7,9], 
              "coughing blood":[1,3,10,11,2,4,7],"high fever":[1,3,10,11,9], "broken bone":[1,3,10,11,2,4,5,7], 
              "head injury":[1,3,10,11,4,7], "vomit":[1,3,10,11,9], "deep cuts":[1,3,10,11,4,9], 
              "breathing issues":[1,3,10,11,2,4,6,7,9], "eye injury":[1,3,10,11,4,9], 
              "severe headaches":[1,3,10,11,9], "dizziness":[1,3,10,11,9], "confusion":[1,3,10,11,9], 
              "clumsiness":[1,3,10,11,9], "chest pain":[1,3,10,11,2,4,5,6,7,9], "severe pain":[1,3,10,11,9], 
              "severe burns":[1,3,10,11,4,6,7,9], "pregnancy bleeding":[1,3,10,11,2,4,5,6,7,9], 
              "testicular pain":[1,3,10,11,9]}
             
emer = ["covid-19 symptoms", "unconscience", "seizure", "life threatening injury", 
      "excessive blood", "coughing blood","high fever", "broken bone", "head injury", 
      "vomit", "deep cuts", "breathing issues", "eye injury", "severe headaches",
      "dizziness", "confusion", "clumsiness", "chest pain", "severe pain", 
      "severe burns", "pregnancy bleeding", "testicular pain"]

nonE = ["dry cough", "low fever", "cuts", "bruises", "sprains", "stomach ache",
       "body ache", "muscle pain", "cold", "difficulty swallowing", "urine pain",
       "asthma", "minor pain", "throat aches", "nosebleeds", "allergies",
       "fungus infection", "ear infection", "minor burns", "shortness of breath",
       "sexually transmitted disease", "menopause", "adhd", "tooth pain", "headaches",
       "migraines", "memory loss"]

Specialist = {"sprains": "Orthopedist", "stomach ache": "Gastroenterologist",
              "muscle pain": "Orthopedist", "urine pain": "Urologist",
              "difficulty swallowing": "Otolaryngologist", "asthma": "Pulmonologist", 
              "allergies": "Allergist", "fungus infection": "Podiatrist", 
              "nosebleeds": "Otolaryngologist", "throat aches": "Otolaryngologist", 
              "ear infection": "Otolaryngologist", "minor burns": "Dermatologist", 
              "sexually transmitted disease": "STD Doctor", "menopause": "Gynecologist", 
              "adhd": "Neurologist", "tooth pain": "Dentist", 
              "shortness of breath": "Cardiologist", "migraines": "Neurologist",
              "memory loss": "Neurologist"}

tally = {}              
works = 1
count = 1
closest = 0
for i in symp:
   if i.lower() in emer:
      for key in data:
         works = 1
         for s in symp:
            if s.lower() in emer:
               for e in symToEquip[s.lower()]:
                  if int(data[key][e]) == 0:
                     works = 0
                  else:
                     if key not in tally:
                        tally[key] = 1
                     else:
                        tally[key] = tally[key] + 1
         if works == 1:
            if Insurance == "Kaiser Permanente":
               for keyK in dataK:
                  if keyK < key:
                     closest = 1
                     print("\nOption", str(count) + ":")
                     count += 1
                     print("Go to", dataK[keyK][0].replace("_"," "))
                  else:
                     print("\nOption", str(count) + ": (If not Time Sensitive)")
                     count += 1
                     print("Go to", dataK[keyK][0].replace("_"," ")) 
                  break
            if closest == 0:
               if Insurance == "Kaiser Permanente":
                  print("\nOption", str(count) + ": (If Time Sensitive)")
               else:
                  print("\nOption", str(count) + ":")
               count += 1
               print("Go to",data[key][0].replace("_"," ")) 
            print("\nOption", str(count) + ":")
            print("Call 911")
            sys.exit()
      max = 0
      key
      for dist in tally:
         if max < tally[dist]:
            max = tally[dist]
      for dist in tally:
         if max == tally[dist]:
            key = dist
            break
      if Insurance == "Kaiser Permanente":
         for keyK in dataK:
            if keyK < key:
               closest = 1
               print("\nOption", str(count) + ":")
               count += 1
               print("Go to", dataK[keyK][0].replace("_"," "))
            else:
               print("\nOption", str(count) + ": (If not Time Sensitive)")
               count += 1
               print("Go to", dataK[keyK][0].replace("_"," ")) 
            break
      if closest == 0:
         if Insurance == "Kaiser Permanente":
            print("\nOption", str(count) + ": (If Time Sensitive)")
         else:
            print("\nOption", str(count) + ":")
         count += 1
         print("Go to",data[key][0].replace("_"," ")) 
      print("\nOption", str(count) + ":")
      print("Call 911")
      sys.exit()
            
count = 1
fin = ""
used = 0
specialists = []
for i in symp:
   if i.lower() in nonE:
      print()
      if Insurance == "PPO" or Insurance == "HMO-Open Access":
         for i2 in symp:
            if i2.lower() in Specialist:
               specialists.append(Specialist[i2.lower()])
               used = 1
         specialists = set(specialists)
         if used == 1:
            print("Option 1: (recommended)")
         if "STD Doctor" in specialists:
            print("If MALE: Make an appointment with Urologist")
            print("If FEMALE: Make an appointment with Gynecologist")
            specialists.remove("STD Doctor")
            if len(specialists) > 0:
               print("And")
         if len(specialists) > 0:
            fin = "Make an appointment with "
         for s in specialists:
            fin += s + ", "
         if fin != "":
            print(fin[:-2])
         if used == 1:
            print("\nOption 2:")
      print("Make an appointment with " + priCare + " @ " + priCareNum)
      sys.exit()