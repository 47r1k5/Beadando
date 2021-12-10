import math
import BMI_Enum
from pathlib import Path

class People:
    def __init__(self, name, sex, age, height, weight, waist, neck,  hip):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.neck = neck
        self.waist = waist
        self.hip = hip

    def bmi_calculator(self)->float:
        bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        print(self.name + "'s BMI is: " + str(bmi) + " kg/m^2")
        return bmi

    def body_fat_calculator(self) -> float:
        bodyFatPercentage=0
        try:
            if self.sex=="m":
                bodyFatPercentage=round(((495 / (1.0324 - 0.19077 * math.log10(self.waist - self.neck) + 
                    0.15456 * math.log10(self.height))) - 450),2)
                print(self.name + "'s Body fat percent is: " + str(bodyFatPercentage) + "%")
            else:
                bodyFatPercentage=round(((495 / (1.0324 - 0.19077 * math.log10(self.waist + self.hip - self.neck) + 
                    0.15456 * math.log10(self.height))) - 450),2)
                print(self.name + "'s Body fat percent is: " + str(bodyFatPercentage) + "%")
            return bodyFatPercentage
        except:
            print("An error has accured! There might be some false data within the following ones: ")
            print("Waist: " + str(self.waist))
            print("Neck: " + str(self.neck))
            print("hip: " + str(self.hip))
            print("You have to try again!")
            return 0

    def bmr_calculator(self,bodyFatPercentage:float)->None:
        bmr=round((370+21.6*(1-bodyFatPercentage/100)*self.weight),2)
        print(self.name + "'s BMR (Basal Metabolic Rate) is: " + str(bmr))

    def decide_bmi(self, bmi:float)->None:
        if self.age<=20:
            if bmi<=BMI_Enum.bmiUnderAgeEnum.UNDERWEIGHT.value:
                bmi=BMI_Enum.bmiUnderAgeEnum.UNDERWEIGHT.name

            elif bmi<=BMI_Enum.bmiUnderAgeEnum.HEALTHY.value:
                bmi=BMI_Enum.bmiUnderAgeEnum.HEALTHY.name

            elif bmi<=BMI_Enum.bmiUnderAgeEnum.RISK_OF_OVERWEIGHT.value:
                bmi=BMI_Enum.bmiUnderAgeEnum.RISK_OF_OVERWEIGHT.name

            else:
                bmi=BMI_Enum.bmiUnderAgeEnum.OVERWEIGHT.name

        else:
            if bmi<=BMI_Enum.bmiAdultEnum.SEVERE_THINNES.value:
                bmi=BMI_Enum.bmiAdultEnum.SEVERE_THINNES.name

            elif bmi<=BMI_Enum.bmiAdultEnum.MODERATE_THINNES.value:
                bmi=BMI_Enum.bmiAdultEnum.MODERATE_THINNES.name

            elif bmi<=BMI_Enum.bmiAdultEnum.MILD_THINNES.value:
                bmi=BMI_Enum.bmiAdultEnum.MILD_THINNES.name

            elif bmi<=BMI_Enum.bmiAdultEnum.NORMAL.value:
                bmi=BMI_Enum.bmiAdultEnum.NORMAL.name

            elif bmi<=BMI_Enum.bmiAdultEnum.OVERWEIGHT.value:
                bmi=BMI_Enum.bmiAdultEnum.OVERWEIGHT.name

            elif bmi<=BMI_Enum.bmiAdultEnum.OBESE_I.value:
                bmi=BMI_Enum.bmiAdultEnum.OBESE_I.name

            elif bmi<=BMI_Enum.bmiAdultEnum.OBESE_II.value:
                bmi=BMI_Enum.bmiAdultEnum.OBESE_II.name

            else:
                bmi=BMI_Enum.bmiAdultEnum.OBESE_III.name

        print("According to the calculator.net, " + self.name + "'s BMI falls into the " + bmi + " category.")

    def write_file(self,file_path:Path)->None:
        if not file_path.exists():
            with open(file_path, "w") as file:
                file.write(str(self.name) + "," + str(self.sex) + "," +
                    str(self.age) + "," + str(self.height) + "," +
                    str(self.weight) + "," + str(self.neck) + "," + str(self.waist) + "," + str(self.hip) + "\n")
            file.close
        else:
            with open(file_path, "a") as file:
                    file.write(str(self.name) + "," + str(self.sex) + "," +
                        str(self.age) + "," + str(self.height) + "," +
                        str(self.weight) + "," + str(self.neck) + "," + str(self.waist) + "," + str(self.hip) + "\n")
            file.close
            

    @classmethod
    def setData(cls):
        return cls(
            str(input("Name : ")),
            cls.setSex(),
            cls.setAge(),
            cls.setHeight(),
            cls.setWeight(),
            cls.setWaist(),
            cls.setNeck(),
            cls.setHip()
        )

    @classmethod
    def setSex(cls)->str:
        sex = ""
        while sex == "":
            try:
                sex = str(input("(Biological) Sex (f - female, m - male): "))
                if sex=="m" or sex=="f":
                    return sex
                sex=""
            except ValueError:
                print("Error! You have to choose between f (female) and m (male). Try again! \n")

    @classmethod
    def setAge(cls) -> int:
        age = 0
        while age == 0:
            try:
                age = int(input("Age (between 100 and 1): "))
                if age>0 and age<100:
                    return age
                age=0
            except ValueError:
                print("Error! Try again!\n")

    @classmethod
    def setHeight(cls)->float:
        height = 0
        while height == 0:
            try:
                height = float(input("Height in cm: "))
                if height>0:
                    return height
                height=0
            except ValueError:
                print("Error! Try again!")

    @classmethod
    def setWeight(cls) ->float:
        weight = 0
        while weight == 0:
            try:
                weight = float(input("Weight in kg: "))
                if weight>0:
                    return weight
                weight=0
            except ValueError:
                print("Error! Try again!")

    @classmethod
    def setWaist(cls)->float:
        waist = 0
        while waist == 0:
            try:
                waist = float(input("Waist in cm: "))
                if waist>0:
                    return waist
                waist=0
            except ValueError:
                print("Error! Try again!")
        return waist

    @classmethod
    def setNeck(cls)->float:
        neck = 0
        while neck == 0:
            try:
                neck = float(input("Neck in cm: "))
                if neck > 0:
                    return neck
                neck=0
            except ValueError:
                print("Error! Try again!")
    
    @classmethod
    def setHip(cls)->float:
        hip=0
        while hip == 0:
            try:
                hip = float(input("Hip in cm: "))
                if hip>0:
                    return hip
                hip=0
            except ValueError:
                print("Error! Try again!")

"""

A két származtatott osztály megoldásával 10-12 órát próbálkoztam, de nem sikerült, ezért hagytam ki.
Folyton azt kaptam hibakódnak, hogy nem találhatóak a konstruktor paraméterei.

class Male(Person):
    def __init__(self, name, sex, age, height, weight, neck, waist) -> None:
        super().__init__( name, sex, age, height, weight, neck, waist)
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.neck = neck
        self.waist = waist
    def male_body_fat(self)
        bodyFatPercentage=round(((495 / (1.0324 - 0.19077 * math.log10(self.waist - self.neck) + 
            0.15456 * math.log10(self.height))) - 450),2)
        print(self.name + "'s Body fat percent is: " + str(bodyFatPercentage) + "%")
        return bodyFatPercentage

class Female(Person):
    def __init__(self, name, sex, age, height, weight, neck, waist, hip) -> None:
        super().__init__(self, name, sex, age, height, weight, neck, waist)
        self.hip=hip
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.neck = neck
        self.waist = waist
        self.hip=hip
    
    def female_body_fat(self)
        bodyFatPercentage=round(((495 / (1.0324 - 0.19077 * math.log10(self.waist + self.hip - self.neck) + 
            0.15456 * math.log10(self.height))) - 450),2)
        print(self.name + "'s Body fat percent is: " + str(bodyFatPercentage) + "%")
        return bodyFatPercentage
"""