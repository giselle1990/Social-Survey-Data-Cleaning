# 🏡 Data Cleaning & Transformation - Housing Subsidy Survey

## 📌 Project Description
This project is part of a Data Science portfolio, focusing on the **cleaning and transformation** of a dataset from a housing subsidy survey. The goal is to process messy data using preprocessing techniques, ensuring data quality for future analysis.

## 📊 Dataset Structure
The original dataset contains information about survey respondents and their housing conditions, including:

- **Persona**: Unique identifier for the respondent.
- **Edad**: Age of the respondent.
- **Género**: Gender identity.
- **Residencia**: Location of residence.
- **Ocupación**: Employment status.
- **Situación Habitacional**: Housing condition (e.g., "Calle", "Alquilada").
- **Conoce Subsidios**: Indicates whether the respondent is aware of available subsidies.
- **Solicitó Subsidios**: Indicates if a subsidy application was submitted.
- **Recibió Subsidios**: Indicates if the respondent received a subsidy.
- **Suficiencia de Alimentos (1-5)**: Scale measuring food sufficiency.
- **Calidad de Alimentos (1-5)**: Scale measuring food quality.

## 🛠️ Data Cleaning Process
The original dataset contained inconsistencies, missing values, and formatting issues that were corrected through:

✅ **Duplicate Removal**: Eliminated repeated entries.  
✅ **Data Type Correction**: Converted age and numerical scales to the correct format.  
✅ **Response Normalization**: Standardized "Yes"/"No" responses.  
✅ **Handling Missing Values**: Filled missing values in key columns with "Unknown."  
✅ **Category Standardization**: Fixed errors in categorical variables.  

## 🚀 How to Run the Code
Follow these steps to clean the dataset:

1️⃣ Clone this repository or download the files.  
2️⃣ Ensure the messy dataset (`encuesta_sucia.csv`) is in the same directory as the script.  
3️⃣ Install the required dependencies:
   ```bash
   pip install pandas numpy
   ```
4️⃣ Run the cleaning script:
   ```bash
   python clean.py
   ```
5️⃣ The cleaned file will be generated as `encuesta_limpia.csv`.

## 📈 Expected Results
After executing the script, you'll obtain a **structured dataset** with consistent values, ready for further analysis in studies on housing subsidies.

---
👤 **Author:** [Your Name]  
📌 This project is part of a Data Science portfolio.
