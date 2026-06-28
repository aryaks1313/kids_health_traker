import matplotlib.pyplot as plt
import streamlit as st

#bmi chart
def bmi_chart(dates,bmi):
    plt.figure(figsize=(6,4))
    plt.plot(dates,bmi,marker='*')
    plt.title('BMI Growth charts')
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.grid(True)
    plt.show()



def nutrition_chart(labels, consumed, required):
    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(labels))
    ax.bar([i - 0.2 for i in x],consumed,width=0.4, label="Consumed")
    ax.bar([i + 0.2 for i in x],required,width=0.4,label="Required")
    ax.set_title("Nutrition Analysis")
    ax.set_ylabel("Amount")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()
    st.pyplot(fig)

