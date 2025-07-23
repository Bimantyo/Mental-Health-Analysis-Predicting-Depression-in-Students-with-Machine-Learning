import streamlit as st 
import pandas as pd
import seaborn as sns 
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Membuat title
    st.title('Aplikasi Early Detection of Depression')

    # Membuat Sub Header
    st.subheader('Page ini mengenai Exploratory Data Analysis dari dataset Student Depression by Bimantyo Arya')

    # Menambahkan Gambar
    image = Image.open('./src/image.jpg')
    st.image(image, caption='The pain you feel today is the strength you will feel tomorrow.')

    # Menampilkan Dataframe
    st.write('### Student Depression Dataset')
    df = pd.read_csv('./src/Student Depression Dataset.csv')
    st.dataframe(df) # dataframe sudah interaktif kalo mau mengembalikan bisa klik titik tiga paling kiri

    # PIE CHART for Gender
    st.write('### Pie Chart of Gender Distribution')
    gender_counts = df['Gender'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio to make it circular
    st.pyplot(fig1)

    # Optional caption
    st.caption('Distribusi jenis kelamin pada dataset.')

    # Membuat Bar Plot 
    # Filter out nilai 0
    filtered_df = df[df['Academic Pressure'] != 0]
    st.write('### Plot Academic Pressure')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Academic Pressure', data=filtered_df)
    st.pyplot(fig)
    st.caption('Distribusi Academic Pressure student berdasarkan skala 1-5, dengan pengecualian nilai 0 yang dianggap sebagai error atau outlier.')

    # Membuat Bar Plot 
    # Filter out nilai Others
    filtered_df = df[df['Sleep Duration'] != 'Others']
    st.write('### Plot Sleep Duration')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Sleep Duration', data=filtered_df)
    st.pyplot(fig)
    st.caption('Distribusi Sleep Duration student memiliki nilai Others yang dianggap sebagai error atau outlier sehingga tidak ditampilkan dalam plot.')
    
    # Membuat Bar Plot 
    st.write('### Plot Suicidal Thoughts')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Have you ever had suicidal thoughts ?', hue='Depression', data=df)
    plt.legend(title='Depression', labels=['No', 'Yes'])
    st.pyplot(fig)
    st.caption('Distribusi Suicidal Thoughts dengan Depression.')

    # Membuat Bar Plot 
    filtered_df = df[df['Dietary Habits'] != 'Others']
    st.write('### Plot Dietary Habits')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Dietary Habits', hue='Depression', data=filtered_df)
    plt.legend(title='Depression', labels=['No', 'Yes'])
    st.pyplot(fig)
    st.caption('Distribusi Dietary Habits dengan Depression.')

if __name__== '__main__':
    run()