import streamlit as st
import pandas as pd

# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.markdown("""<link rel="stylesheet" href="assets/css/styles.css" type="text/css"/>
""", unsafe_allow_html=True)
# st.markdown(
# """<style> 
            
# div.st-emotion-cache-vdokb0 {
#     font-family: "Source Sans Pro", sans-serif;
#     margin-bottom: -1.3rem;
# }

# div.st-emotion-cache-13ln4jf {
#     padding: 1rem 1rem 10rem;
# }

# div.st-emotion-cache-dvne4q {
#     padding: 3rem 1.5rem;
# }

# button.st-emotion-cache-13ejsyy{
#     margin-left: 29px;
# }

# span.st-emotion-cache-10trblm {
#     margin-left: 310px;
# }

# div.user-select-none.svg-container{
#     position: relative;
#     width: 700px;
#     height: 400px;
# } </style>""", unsafe_allow_html=True)

with st.sidebar:
    # st.image('https://www.vabysmo-hcp.com/content/dam/gene/vabysmo-hcp/logos/vabysmo-logo-og.genecoreimg.1200.png')
    drugs_selected = st.multiselect(
    "Drugs Selected",
    ["Drug 1", "Drug 2", "Drug 3", "Drug 4","Drug 5"],
    ["Drug 1", "Drug 2", "Drug 3", "Drug 4","Drug 5"])
    disease_indication=st.sidebar.selectbox('Disease Indication',['WET AMD','DME'])
    time_horizon=st.sidebar.selectbox('Time Horizon (in Years)',['1','2','3','4','5'])
    patient_support=st.sidebar.selectbox('Patient Support',['Yes','No'])
    if patient_support == "Yes":
     drug1_cost_per_vial=30000  #---Drug 1 = Faricimab
     drug2_cost_per_vial=24000 #---Drug 2 = Aflibercept
     drug3_cost_per_vial=35000 #---Drug 3 = Brolucizumab
     drug4_cost_per_vial=25000  #---Drug 4 = Ranibizumab
     drug5_cost_per_vial=20000  #---Drug 5 = Rani Biosimilar
    
    else:
     drug1_cost_per_vial=75000  #---Drug 1 = Faricimab
     drug2_cost_per_vial=60000 #---Drug 2 = Aflibercept
     drug3_cost_per_vial=35000 #---Drug 3 = Brolucizumab
     drug4_cost_per_vial=25000  #---Drug 4 = Ranibizumab
     drug5_cost_per_vial=20000  #---Drug 5 = Rani Biosimilar
    
    naive_switch=st.sidebar.selectbox('Naive/Switch',['Naive','Switch'])
    clinical_status=st.sidebar.selectbox('Clinical Status',['Per Label','RWE'])
   
    if(disease_indication=="WET AMD" and time_horizon=="1" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "6", "Drug 2": "8", "Drug 3": "8", "Drug 4": "12", "Drug 5": "12"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=6
        drug2_dosage=8
        drug3_dosage=8
        drug4_dosage=12
        drug5_dosage=12

    elif(disease_indication=="WET AMD" and time_horizon=="2" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "9", "Drug 2": "14", "Drug 3": "12", "Drug 4": "24", "Drug 5": "24"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=9
        drug2_dosage=14
        drug3_dosage=12
        drug4_dosage=24
        drug5_dosage=24

    elif(disease_indication=="WET AMD" and time_horizon=="3" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "12", "Drug 2": "20", "Drug 3": "16", "Drug 4": "36", "Drug 5": "36"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=12
        drug2_dosage=20
        drug3_dosage=16
        drug4_dosage=36
        drug5_dosage=36

    elif(disease_indication=="WET AMD" and time_horizon=="4" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "15", "Drug 2": "26", "Drug 3": "20", "Drug 4": "48", "Drug 5": "48"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=15
        drug2_dosage=26
        drug3_dosage=20
        drug4_dosage=48
        drug5_dosage=48
    
    elif(disease_indication=="WET AMD" and time_horizon=="5" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "18", "Drug 2": "32", "Drug 3": "24", "Drug 4": "60", "Drug 5": "60"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=18
        drug2_dosage=32
        drug3_dosage=24
        drug4_dosage=60
        drug5_dosage=60
    
    elif(disease_indication=="DME" and time_horizon=="1" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "6", "Drug 2": "9", "Drug 3": "9", "Drug 4": "12", "Drug 5": "12"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=6
        drug2_dosage=9
        drug3_dosage=9
        drug4_dosage=12
        drug5_dosage=12
    
    
    elif(disease_indication=="DME" and time_horizon=="2" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "9", "Drug 2": "15", "Drug 3": "13", "Drug 4": "24", "Drug 5": "24"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=9
        drug2_dosage=15
        drug3_dosage=13
        drug4_dosage=24
        drug5_dosage=24
    
    
    elif(disease_indication=="DME" and time_horizon=="3" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "12", "Drug 2": "21", "Drug 3": "17", "Drug 4": "36", "Drug 5": "36"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=12
        drug2_dosage=21
        drug3_dosage=17
        drug4_dosage=36
        drug5_dosage=36
    
    
    elif(disease_indication=="DME" and time_horizon=="4" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "15", "Drug 2": "27", "Drug 3": "21", "Drug 4": "48", "Drug 5": "48"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=15
        drug2_dosage=27
        drug3_dosage=21
        drug4_dosage=48
        drug5_dosage=48
    
    
    elif(disease_indication=="DME" and time_horizon=="5" and naive_switch=="Naive" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "18", "Drug 2": "33", "Drug 3": "25", "Drug 4": "60", "Drug 5": "60"}
        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=18
        drug2_dosage=33
        drug3_dosage=25
        drug4_dosage=60
        drug5_dosage=60

    elif(disease_indication=="WET AMD" and naive_switch=="Switch" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "3", "Drug 2": "6", "Drug 3": "4", "Drug 4": "12", "Drug 5": "12"}        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=3
        drug2_dosage=6
        drug3_dosage=4
        drug4_dosage=12
        drug5_dosage=12
    
    elif(disease_indication=="DME" and naive_switch=="Switch" and clinical_status=="Per Label"):
        user_info = {"Drug 1": "3", "Drug 2": "6", "Drug 3": "4", "Drug 4": "12", "Drug 5": "12"}        
        table = "<table><tr><th style='width:70px'>Drug</th><th style='width:70px'>Dosage</th></tr>"
        for key in user_info.keys():
            table += f"<tr><td style='width:70%'>{key}</td><td style='width:70%'>{user_info[key]}</td></tr>"
        table += "</table>"
        st.sidebar.markdown(table, unsafe_allow_html=True)
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        drug1_dosage=3
        drug2_dosage=6
        drug3_dosage=4
        drug4_dosage=12
        drug5_dosage=12

    elif(clinical_status=="RWE"):
        if 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)

        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
        
        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
            drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
            drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
        
        elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
            drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
           
    
    procedure_cost =st.sidebar.selectbox('Procedure Cost',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000','₹21,000','₹22,000','₹23,000','₹24,000','₹25,000','₹26,000','₹27,000','₹28,000','₹29,000','₹30,000'])
    oct_cost = st.sidebar.selectbox('OCT Cost',['₹0','₹200','₹300','₹500','₹700','₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
    consulting_charges = st.sidebar.selectbox('Consultating Charges',['₹0','₹200','₹300','₹500','₹700','₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
    miscellaneous_cost = st.sidebar.selectbox('Miscellaneous Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹100','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
    travel_cost = st.sidebar.selectbox('Travel Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹100','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
    food_cost = st.sidebar.selectbox('Food Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹100','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
    patient_lost_opportunity_cost = st.sidebar.selectbox('Lost Opportunity Cost/Day (Patient)',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000'])
    caregiver_lost_opportunity_cost = st.sidebar.selectbox('Lost Opportunity Cost/Day (Caregiver)',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000'])
    #................................Final Costs...........................................................
    procedure_cost=procedure_cost[1:]
    if ',' in procedure_cost:
        procedure_cost=procedure_cost.replace(',','')
        procedure_cost=int(procedure_cost)
    else:
        procedure_cost=int(procedure_cost)

    consulting_charges=int(consulting_charges[1:])
    oct_cost=int(oct_cost[1:])
    miscellaneous_cost=int(miscellaneous_cost[1:])
    travel_cost=int(travel_cost[1:])
    food_cost=int(food_cost[1:])

    patient_lost_opportunity_cost=patient_lost_opportunity_cost[1:]
    if ',' in patient_lost_opportunity_cost:
        patient_lost_opportunity_cost=patient_lost_opportunity_cost.replace(',','')
        patient_lost_opportunity_cost=int(patient_lost_opportunity_cost)
    else:
        patient_lost_opportunity_cost=int(patient_lost_opportunity_cost)

    caregiver_lost_opportunity_cost=caregiver_lost_opportunity_cost[1:]
    if ',' in caregiver_lost_opportunity_cost:
        caregiver_lost_opportunity_cost=caregiver_lost_opportunity_cost.replace(',','')
        caregiver_lost_opportunity_cost=int(caregiver_lost_opportunity_cost)
    else:
        caregiver_lost_opportunity_cost=int(caregiver_lost_opportunity_cost)

    #--------Drug 1----------------------------------------------------------------------------------------
    drug1_dosage=int(drug1_dosage)
    drug1_dosage_half=drug1_dosage/2
    drug1_total_package_cost=(drug1_cost_per_vial+procedure_cost)*drug1_dosage
    drug1_total_consulting_charges=consulting_charges*(drug1_dosage+drug1_dosage_half)
    drug1_total_oct_charges=oct_cost*(drug1_dosage+drug1_dosage_half)
    drug1_total_travel_food_cost=(travel_cost+food_cost+miscellaneous_cost)*(drug1_dosage+drug1_dosage_half)
    drug1_total_opportunity_cost_lost=(patient_lost_opportunity_cost*(drug1_dosage+drug1_dosage_half))+(caregiver_lost_opportunity_cost*(drug1_dosage+drug1_dosage_half))

    drug1_total_cost_per_patient=drug1_total_package_cost+drug1_total_consulting_charges+drug1_total_oct_charges+drug1_total_travel_food_cost+drug1_total_opportunity_cost_lost
    
    #--------Drug 2----------------------------------------------------------------------------------------
    drug2_dosage=int(drug2_dosage)
    drug2_dosage_half=drug2_dosage/2
    drug2_total_package_cost=(drug2_cost_per_vial+procedure_cost)*drug2_dosage
    drug2_total_consulting_charges=consulting_charges*(drug2_dosage+drug2_dosage_half)
    drug2_total_oct_charges=oct_cost*(drug2_dosage+drug2_dosage_half)
    drug2_total_travel_food_cost=(travel_cost+food_cost+miscellaneous_cost)*(drug2_dosage+drug2_dosage_half)
    drug2_total_opportunity_cost_lost=(patient_lost_opportunity_cost*(drug2_dosage+drug2_dosage_half))+(caregiver_lost_opportunity_cost*(drug2_dosage+drug2_dosage_half))

    drug2_total_cost_per_patient=drug2_total_package_cost+drug2_total_consulting_charges+drug2_total_oct_charges+drug2_total_travel_food_cost+drug2_total_opportunity_cost_lost
    
    #--------Drug 3----------------------------------------------------------------------------------------
    drug3_dosage=int(drug3_dosage)
    drug3_dosage_half=drug3_dosage/2
    drug3_total_package_cost=(drug3_cost_per_vial+procedure_cost)*drug3_dosage
    drug3_total_consulting_charges=consulting_charges*(drug3_dosage+drug3_dosage_half)
    drug3_total_oct_charges=oct_cost*(drug3_dosage+drug3_dosage_half)
    drug3_total_travel_food_cost=(travel_cost+food_cost+miscellaneous_cost)*(drug3_dosage+drug3_dosage_half)
    drug3_total_opportunity_cost_lost=(patient_lost_opportunity_cost*(drug3_dosage+drug3_dosage_half))+(caregiver_lost_opportunity_cost*(drug3_dosage+drug3_dosage_half))

    drug3_total_cost_per_patient=drug3_total_package_cost+drug3_total_consulting_charges+drug3_total_oct_charges+drug3_total_travel_food_cost+drug3_total_opportunity_cost_lost

    
#--------Drug 4----------------------------------------------------------------------------------------
    drug4_dosage=int(drug4_dosage)
    drug4_dosage_half=drug4_dosage/2
    drug4_total_package_cost=(drug4_cost_per_vial+procedure_cost)*drug4_dosage
    drug4_total_consulting_charges=consulting_charges*(drug4_dosage+drug4_dosage_half)
    drug4_total_oct_charges=oct_cost*(drug4_dosage+drug4_dosage_half)
    drug4_total_travel_food_cost=(travel_cost+food_cost+miscellaneous_cost)*(drug4_dosage+drug4_dosage_half)
    drug4_total_opportunity_cost_lost=(patient_lost_opportunity_cost*(drug4_dosage+drug4_dosage_half))+(caregiver_lost_opportunity_cost*(drug4_dosage+drug4_dosage_half))

    drug4_total_cost_per_patient=drug4_total_package_cost+drug4_total_consulting_charges+drug4_total_oct_charges+drug4_total_travel_food_cost+drug4_total_opportunity_cost_lost
#--------Drug 5----------------------------------------------------------------------------------------
    drug5_dosage=int(drug5_dosage)
    drug5_dosage_half=drug5_dosage/2
    drug5_total_package_cost=(drug5_cost_per_vial+procedure_cost)*drug5_dosage
    drug5_total_consulting_charges=consulting_charges*(drug5_dosage+drug5_dosage_half)
    drug5_total_oct_charges=oct_cost*(drug5_dosage+drug5_dosage_half)
    drug5_total_travel_food_cost=(travel_cost+food_cost+miscellaneous_cost)*(drug5_dosage+drug5_dosage_half)
    drug5_total_opportunity_cost_lost=(patient_lost_opportunity_cost*(drug5_dosage+drug5_dosage_half))+(caregiver_lost_opportunity_cost*(drug5_dosage+drug5_dosage_half))

    drug5_total_cost_per_patient=drug5_total_package_cost+drug5_total_consulting_charges+drug5_total_oct_charges+drug5_total_travel_food_cost+drug5_total_opportunity_cost_lost

    if 'Drug 1' not in drugs_selected:
        drug1_total_package_cost=0
        drug1_total_consulting_charges=0
        drug1_total_oct_charges=0
        drug1_total_travel_food_cost=0
        drug1_total_opportunity_cost_lost=0
        drug1_total_cost_per_patient=0


    if 'Drug 2' not in drugs_selected:
        drug2_total_package_cost=0
        drug2_total_consulting_charges=0
        drug2_total_oct_charges=0
        drug2_total_travel_food_cost=0
        drug2_total_opportunity_cost_lost=0
        drug2_total_cost_per_patient=0


    if 'Drug 3' not in drugs_selected:
        drug3_total_package_cost=0
        drug3_total_consulting_charges=0
        drug3_total_oct_charges=0
        drug3_total_travel_food_cost=0
        drug3_total_opportunity_cost_lost=0
        drug3_total_cost_per_patient=0

    if 'Drug 4' not in drugs_selected:
        drug4_total_package_cost=0
        drug4_total_consulting_charges=0
        drug4_total_oct_charges=0
        drug4_total_travel_food_cost=0
        drug4_total_opportunity_cost_lost=0
        drug4_total_cost_per_patient=0
    
    if 'Drug 5' not in drugs_selected:
        drug5_total_package_cost=0
        drug5_total_consulting_charges=0
        drug5_total_oct_charges=0
        drug5_total_travel_food_cost=0
        drug5_total_opportunity_cost_lost=0
        drug5_total_cost_per_patient=0

    button_result=st.button("Apply Changes")
    print("Drug 1")
    print("Total Package Cost",drug1_total_package_cost)
    print("Total Consulting Charges",drug1_total_consulting_charges)
    print("Total Oct Charges",drug1_total_oct_charges)
    print("Travel and Food Cost",drug1_total_travel_food_cost)
    print("Total Opportunity Cost Lost",drug1_total_opportunity_cost_lost)
    print("Total Cost/Patient",drug1_total_cost_per_patient)
    print()
    print()

    print("Drug 2")
    print("Total Package Cost",drug2_total_package_cost)
    print("Total Consulting Charges",drug2_total_consulting_charges)
    print("Total Oct Charges",drug2_total_oct_charges)
    print("Travel and Food Cost",drug2_total_travel_food_cost)
    print("Total Opportunity Cost Lost",drug2_total_opportunity_cost_lost)
    print("Total Cost/Patient",drug2_total_cost_per_patient)
    print()
    print()

    print("Drug 3")
    print("Total Package Cost",drug3_total_package_cost)
    print("Total Consulting Charges",drug3_total_consulting_charges)
    print("Total Oct Charges",drug3_total_oct_charges)
    print("Travel and Food Cost",drug3_total_travel_food_cost)
    print("Total Opportunity Cost Lost",drug3_total_opportunity_cost_lost)
    print("Total Cost/Patient",drug3_total_cost_per_patient)
    print()
    print()

    print("Drug 4")
    print("Total Package Cost",drug4_total_package_cost)
    print("Total Consulting Charges",drug4_total_consulting_charges)
    print("Total Oct Charges",drug4_total_oct_charges)
    print("Travel and Food Cost",drug4_total_travel_food_cost)
    print("Total Opportunity Cost Lost",drug4_total_opportunity_cost_lost)
    print("Total Cost/Patient",drug4_total_cost_per_patient)
    print()
    print()

    print("Drug 5")
    print("Total Package Cost",drug5_total_package_cost)
    print("Total Consulting Charges",drug5_total_consulting_charges)
    print("Total Oct Charges",drug5_total_oct_charges)
    print("Travel and Food Cost",drug5_total_travel_food_cost)
    print("Total Opportunity Cost Lost",drug5_total_opportunity_cost_lost)
    print("Total Cost/Patient",drug5_total_cost_per_patient)

    print()
    print()
# Main pag5
st.title('I-Open')
data=pd.read_csv('Display_data.csv')
if button_result:
        data.loc[0,'Total Package Cost']=drug1_total_package_cost
        data.loc[0,'Consulting Charges']=drug1_total_consulting_charges
        data.loc[0,'OCT Charges']=drug1_total_oct_charges
        data.loc[0,'Travel and Food Costs']=drug1_total_travel_food_cost
        data.loc[0,'Total Opportunity Cost Lost']=drug1_total_opportunity_cost_lost
        data.loc[0,'Total Cost/Patient']=drug1_total_cost_per_patient
    
        data.loc[1,'Total Package Cost']=drug2_total_package_cost
        data.loc[1,'Consulting Charges']=drug2_total_consulting_charges
        data.loc[1,'OCT Charges']=drug2_total_oct_charges
        data.loc[1,'Travel and Food Costs']=drug2_total_travel_food_cost
        data.loc[1,'Total Opportunity Cost Lost']=drug2_total_opportunity_cost_lost
        data.loc[1,'Total Cost/Patient']=drug2_total_cost_per_patient

        data.loc[2,'Total Package Cost']=drug3_total_package_cost
        data.loc[2,'Consulting Charges']=drug3_total_consulting_charges
        data.loc[2,'OCT Charges']=drug3_total_oct_charges
        data.loc[2,'Travel and Food Costs']=drug3_total_travel_food_cost
        data.loc[2,'Total Opportunity Cost Lost']=drug3_total_opportunity_cost_lost
        data.loc[2,'Total Cost/Patient']=drug3_total_cost_per_patient

        data.loc[3,'Total Package Cost']=drug4_total_package_cost
        data.loc[3,'Consulting Charges']=drug4_total_consulting_charges
        data.loc[3,'OCT Charges']=drug4_total_oct_charges
        data.loc[3,'Travel and Food Costs']=drug4_total_travel_food_cost
        data.loc[3,'Total Opportunity Cost Lost']=drug4_total_opportunity_cost_lost
        data.loc[3,'Total Cost/Patient']=drug4_total_cost_per_patient

        data.loc[4,'Total Package Cost']=drug5_total_package_cost
        data.loc[4,'Consulting Charges']=drug5_total_consulting_charges
        data.loc[4,'OCT Charges']=drug5_total_oct_charges
        data.loc[4,'Travel and Food Costs']=drug5_total_travel_food_cost
        data.loc[4,'Total Opportunity Cost Lost']=drug5_total_opportunity_cost_lost
        data.loc[4,'Total Cost/Patient']=drug5_total_cost_per_patient
        # df_html = data.to_html(index=False)
        # st.write(df_html, unsafe_allow_html=True)
        # st.markdown('&nbsp;')
#         import plotly.graph_objects as go

#         # Define your data
#         graph_drugs = data['Drugs'].to_list()
#         graph_total_package_cost = data['Total Package Cost'].to_list()  
#         graph_consulting_charges = data['Consulting Charges'].to_list()  
#         graph_oct_charges = data['OCT Charges'].to_list()  
#         graph_travel_and_food_costs = data['Travel and Food Costs'].to_list()  
#         graph_total_opportunity_cost_lost = data['Total Opportunity Cost Lost'].to_list() 
#         graph_total_cost_per_patient=data['Total Cost/Patient'].to_list()

#         # Create the bar chart
#         fig = go.Figure(data=[
#             go.Bar(name='Total Package Cost', x=graph_drugs, y=graph_total_package_cost),
#             go.Bar(name='Consulting Charges', x=graph_drugs, y=graph_consulting_charges),
#             go.Bar(name='OCT Charges', x=graph_drugs, y=graph_oct_charges),
#             go.Bar(name='Travel and Food Costs', x=graph_drugs, y=graph_travel_and_food_costs),
#             go.Bar(name='Total Opportunity Cost Lost', x=graph_drugs, y=graph_total_opportunity_cost_lost),
#             go.Bar(name='Total Cost/Patient', x=graph_drugs, y=graph_total_cost_per_patient)
#         ])

#         # Change the bar mode
#         fig.update_layout(barmode='group')
#         st.write(fig)
        
#         st.dataframe(data,hide_index=True)
#         store_data=data.copy()
#         store_data.to_csv('Display_data.csv',index=False)

# else:
#     # df_html = data.to_html(index=False)
#     # st.write(df_html, unsafe_allow_html=True)
#     # st.markdown('&nbsp;')
#     st.dataframe(data,hide_index=True)
        import plotly.graph_objects as go

        # Define your data
        graph_drugs = data['Drugs'].to_list()
        graph_total_package_cost = [i/100000 for i in data['Total Package Cost'].to_list()]  
        graph_consulting_charges = [i/100000 for i in data['Consulting Charges'].to_list()]  
        graph_oct_charges = [i/100000 for i in data['OCT Charges'].to_list()]  
        graph_travel_and_food_costs = [i/100000 for i in data['Travel and Food Costs'].to_list()]  
        graph_total_opportunity_cost_lost = [i/100000 for i in data['Total Opportunity Cost Lost'].to_list()] 
        graph_total_cost_per_patient=[i/100000 for i in data['Total Cost/Patient'].to_list()]
        # graph_drugs = data['Drugs'].to_list()
        # graph_total_package_cost = [f"{i/100000:.2f}L" for i in data['Total Package Cost'].to_list()]  
        # graph_consulting_charges = [f"{i/100000:.2f}L" for i in data['Consulting Charges'].to_list()]  
        # graph_oct_charges = [f"{i/100000:.2f}L" for i in data['OCT Charges'].to_list()]  
        # graph_travel_and_food_costs = [f"{i/100000:.2f}L" for i in data['Travel and Food Costs'].to_list()]  
        # graph_total_opportunity_cost_lost = [f"{i/100000:.2f}L" for i in data['Total Opportunity Cost Lost'].to_list()] 
        # graph_total_cost_per_patient=[f"{i/100000:.2f}L" for i in data['Total Cost/Patient'].to_list()]

        # Create the bar chart
        fig = go.Figure(data=[
            go.Bar(name='Total Package Cost', x=graph_drugs, y=graph_total_package_cost, hovertemplate='%{y:.2f} L',text=graph_total_package_cost, textposition='outside'),
            go.Bar(name='Consulting Charges', x=graph_drugs, y=graph_consulting_charges, hovertemplate='%{y:.2f} L',text=graph_consulting_charges, textposition='outside'),
            go.Bar(name='OCT Charges', x=graph_drugs, y=graph_oct_charges, hovertemplate='%{y:.2f} L',text=graph_oct_charges, textposition='outside'),
            go.Bar(name='Travel and Food Costs', x=graph_drugs, y=graph_travel_and_food_costs, hovertemplate='%{y:.2f} L',text=graph_travel_and_food_costs, textposition='outside'),
            go.Bar(name='Total Opportunity Cost Lost', x=graph_drugs, y=graph_total_opportunity_cost_lost, hovertemplate='%{y:.2f} L',text=graph_total_opportunity_cost_lost, textposition='outside'),
            go.Bar(name='Total Cost/Patient', x=graph_drugs, y=graph_total_cost_per_patient, hovertemplate='%{y:.2f} L',text=graph_total_cost_per_patient, textposition='outside')
        ])

        # Change the bar mode
        fig.update_layout(
            barmode='group',
            yaxis=dict(
                tickformat=',.2f',
                title='Value in Lakhs'
            )
        )

        st.write(fig)

        st.dataframe(data,hide_index=True)
        store_data=data.copy()
        store_data.to_csv('Display_data.csv',index=False)

else:
    # df_html = data.to_html(index=False)
    # st.write(df_html, unsafe_allow_html=True)
    # st.markdown('&nbsp;')
    st.dataframe(data,hide_index=True)

