import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

st.title('Irfadillah Afni Nurvita')
with st.sidebar:
    selected = option_menu("",["About Me",'Experience','Education','Contact'], 
        icons=['person', '', '', 'phone'], menu_icon="cast", default_index=1)
    selected
    
if selected == 'About Me':
    st.write('''
    
Hello, my name is Irfadillah Afni Nurvita, I am 25 years old, I am a fresh graduate from the
Universitas Terbuka, majoring in Computer Information Systems. I have experience working in the
production department of a pharmaceutical manufacturing company for 2.5 years, then worked as a QC
helper for 1 year. And now as an intern in Japan in the field of electroplating and have also participated
in several bootcamp activities about data science, graphic design, etc. At the bootcamp about data science
that I attended, I learned about data processing techniques, machine learning, data visualization, industrial
analysis, data modeling, data clustering, Big data, Statistical programming, Feature Engineering, Evaluation Models,
and Improvement. I am a contract employee, while studying and have now graduated with a bachelor's degree in computer
information systems study program from the Universitas Terbuka. Likes taking part in seminars that involve technology,
scholarship and self-development.

    ''')

    
elif selected == 'Experience':
    st.write('''

    
- **Manufacture • Electro Platting • Fine Tech Takahashi Co.,Ltd.**
 
    Oktober 2022 – Sekarang | Chiba, Japan.

Here I have the status of an intership trainee, who gets a jobdesk as
an electroplating operator or coating materials with electric current and chemical coatings.
  
    
- **Quality Control • QC Helper • PT. Kalbe Farma.**

    Desember 2020 – Januari 2022 | Cikarang, Indonesia.
 
 Here I work as a QC helper in microbiology tasked with assisting analysts in ensuring the products
produced meet the set standards. Such as preparing equipment needed to carry out analysis,
helping monitor the production process, helping check product quality, helping monitor raw materials
before they enter the warehouse, helping control documentation of QC activities, maintaining laboratory cleanliness,
calibrating laboratory equipment, and QC helpers are also tasked with detecting,
monitor, and manage microorganisms that have the potential to cause foodborne illnesses.


- **Manufacture • Operator produksi • PT. Dankos Farma.** 

April 2019 – November 2020 | Jakarta, Indonesia.

Here I work as a production operator in the secondary packaging section, so my responsibility
here is to package products, manage and fill out product documents, and ensure that the products 
we package are of high quality and meet predetermined targets.


- **Manufacture • Operator produksi • PT. Pharos Indonesia.**


November 2017 – November 2018 | Jakarta, Indonesia.

Here I work as a production operator in the packer section, with the position as THP / Weighing packing
results, my responsibility here is weighing packaging results manually and ensuring that the contents of 
each product are complete, then filling in the product documents and i am responsible for the product's operation.

    ''')
    
elif selected == 'Education':    
    st.write('''
    **Bootcamp of Data Science** (October 2024 - Mey 2025)
    - Learn comprehensive data analyst skills, from data analysis,
    data visualization, data clustering, machine learning, to big data to uncover important insights.
    
    **Universitas Terbuka** (2019 - 2024)
    - Bachelor of Computer Information Systems
    - Study Program of Computer Information Systems
    - GPA: 3.34/4.00
    - Learn about the basics of enterprise systems and issues in their implementation,
    how the role of enterprise systems plays in integrating business functional areas.
    ''')
    
elif selected == 'Contact':
    st.write('''
    **Email:**
    [irfadillahafninurvita@gmail.com](irfadillahafninurvita@gmail.com)
    
    **LinkedIn:**
    [Irfadillah Afni Nurvita](https://www.linkedin.com/in/irfadillah-afni-nurvita/)
    
    **Whatsapp:**
    [082123970898](https://wa.me/6282123970898)
    ''')