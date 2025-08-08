# :sunny: Mental Health Analysis: Predicting Depression in Students with Machine Learning

Hello! I’m Bima, and this project is designed to predict students who may be at risk of experiencing depression, enabling early preventive measures and appropriate interventions for those showing signs of mental health challenges. By leveraging machine learning models, the process of identifying depression risk becomes faster, data-driven, and more accurate—supporting efforts to improve students’ overall mental well-being.

## 🛠️ Repository Outline

This repository contains the following files:

1. `README.md` – General overview of the project.  
2. `Milestone_2.ipynb` – Main notebook for data processing and modeling
3. `Milestone_2_dataset.csv` = The original dataset.
4. `Milestone_2_inference.ipynb` = Notebook for running inference on new data.
5. `best_svm_pipeline_final.pkl` - The model that is used on this project.
6. `deployment_new` - Folder that contain all deployment files to Hugging Face

## :eyes: Problem Background

Mental health has become an increasingly prominent issue in today’s society. While awareness in the past was limited, public understanding of the importance of mental well-being has grown significantly in recent years. Mental health plays a critical role in shaping an individual’s lifestyle, mindset, behavior, and even physical condition. Recognizing and monitoring mental health from an early stage is essential in preventing more serious issues and promoting overall well-being.

This project focuses on predicting the likelihood of depression among students by applying machine learning models. The prediction is based on a range of features available in the dataset, including academic pressure, study satisfaction, sleep duration, and other social and psychological factors. By leveraging data-driven insights, the project aims to enable early detection, facilitate timely interventions, and ultimately support efforts to improve students’ mental health and quality of life.

## 📊 Project Highlights

- Students with healthy diets tend to be less prone to depression, while those with moderate diets show a majority experiencing depression. Students with unhealthy diets are predominantly affected by depression.
- A significant number of students sleep less than 5 hours, with 2,065 students experiencing both high academic pressure and short sleep duration—indicating a link between high academic pressure and reduced sleep.
- Students with depression tend to have higher financial stress, also tend to have higher academic pressure

## :computer: Data
The data source used comes from [kaggle](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)

The dataset contains 18 columns and a total of 27.9 thousand rows. No duplicate entries were found; however, there are three missing values in the financial_stress column. Although the dataset includes several professions, non-student professions are represented by only a small number of rows and are not statistically significant within the population. Therefore, this project focuses exclusively on the student profession to avoid potential outliers or bias in the analysis.

In the columns academic_pressure, cgpa, financial_stress, and study_satisfaction, there are entries with a value of 0, which may indicate erroneous or invalid inputs. These will be filtered out to ensure only valid and reliable data is used. The majority of the data exhibits a normal distribution.

## :rocket: Reference

Reference for this project 

- https://ayosehat.kemkes.go.id/pentingnya-kesehatan-mental-bagi-remaja
- https://hiinstitute.or.id/pentingnya-kesehatan-mental-di-era-modern-2/
- https://ejournal.fkm.unsri.ac.id/index.php/jikm/article/view/241
- https://rgrfm.tulungagung.go.id/mental-illness-penyebab-dan-dampak-yang-perlu-diketahui/

## :dart: Model Deployment

For model deployment can be accessed [here](https://huggingface.co/spaces/Bimaarya/student-depression-awareness)

Usage Instructions

1. Click the link provided below.
2. In the navigation bar, switch to the Prediction section.
3. Fill in the parameters according to your personal condition.
4. Click Predict.
5. The model will generate a prediction based on the parameters you entered. A result of 1 indicates that you are predicted to be experiencing depression.

## 🛠 Tools & Skills

- **Python**
- **pandas, numpy** — data manipulation
- **matplotlib, seaborn** — data visualization
- **scikit-learn** - data processing
- **cat-boost** - Modeling


## :necktie:  Let’s Get To Know Each Other!

I welcome any feedback, suggestions, or opportunities for collaboration. If you would like to connect or discuss ideas, feel free to reach out.

**Bimantyo Arya Majid**  
[Email](bimantyoarya13@gmail.com) | [LinkedIn](https://www.linkedin.com/in/bimantyoarya/)
