import streamlit as st

# Custom CSS for enhanced UI
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .sidebar .sidebar-content a {
        color: white;
    }
    .sidebar .sidebar-content a:hover {
        color: #3498db;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        color: white;
    }
    h1 {
        color: #3498db;
        text-align: center;
    }
    .content-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display the main page with navigation buttons
def main_page():
    st.title("Ewing Sarcoma: A Comprehensive Overview")
    st.write("Ewing sarcoma is a rare and aggressive type of cancer that primarily affects the bones or the soft tissue surrounding the bones (soft tissue sarcoma). It is most commonly diagnosed in children, teenagers, and young adults, but it can occur at any age.")
    st.image("WhatsApp Image 2024-08-27 at 6.04.21 PM.jpeg", use_column_width=True)
# Function to display Content1 page
def content1_page():
    st.title("Ewing Sarcoma: A Comprehensive Overview")
    st.markdown("<h2>Epidemiology:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Age Group**: Primarily affects individuals between 10 and 20 years of age.
    - **Incidence**: Approximately 1-3 cases per million per year.
    - **Gender**: Slightly more common in males than females.
    - **Ethnicity**: Predominantly affects individuals of European ancestry, with significantly lower incidence in African and Asian populations.
    """, unsafe_allow_html=True)

    st.markdown("<h2>Pathophysiology:</h2>", unsafe_allow_html=True)
    st.markdown("""
    Ewing sarcoma is characterized by the presence of a specific chromosomal translocation, typically between chromosomes 11 and 22, resulting in the EWSR1-FLI1 fusion gene. This abnormal gene leads to uncontrolled cell growth and contributes to the malignancy of the tumor.
    """, unsafe_allow_html=True)
    st.image("WhatsApp Image 2024-08-27 at 7.07.45 PM.jpeg", use_column_width=True)
    st.markdown("<h2>Common Sites of Occurrence:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Bone**: The most common sites include the pelvis, femur (thigh bone), tibia (shin bone), and humerus (upper arm bone).
    - **Soft Tissue**: Ewing sarcoma can also occur in soft tissues, such as muscles or the chest wall (Askin tumor).
    """, unsafe_allow_html=True)

    st.markdown("<h2>Clinical Presentation:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Pain**: Persistent localized pain, often mistaken for a sports injury or growing pains.
    - **Swelling**: Visible swelling or a palpable mass at the tumor site.
    - **Systemic Symptoms**: Fever, fatigue, weight loss, and night sweats may occur, especially if the disease has metastasized.
    - **Neurological Symptoms**: If the tumor is located near the spine, it may cause nerve compression, leading to pain, weakness, or paralysis.
    """, unsafe_allow_html=True)

    st.markdown("<h2>Diagnosis:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Imaging Studies**:
        - **X-rays**: Initial imaging to detect bone abnormalities.
        - **MRI/CT scans**: Detailed imaging to assess the tumor's size, extent, and involvement of surrounding tissues.
        - **Bone Scan/PET scan**: To detect metastasis.
    - **Biopsy**:
        - A definitive diagnosis is made by biopsy, where a sample of the tumor is examined under a microscope.
        - Immunohistochemistry and molecular testing (such as fluorescence in situ hybridization, or FISH) are used to detect the EWSR1-FLI1 fusion gene.
    """, unsafe_allow_html=True)
    st.image("WhatsApp Image 2024-08-27 at 7.11.04 PM.jpeg", use_column_width=True)

    st.markdown("<h2>Staging:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Localized Disease**: Tumor confined to the site of origin without spread.
    - **Metastatic Disease**: Tumor has spread to other parts of the body, such as the lungs, other bones, or bone marrow.
    """, unsafe_allow_html=True)

    st.markdown("<h2>Treatment:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Multimodal Approach**:
        - **Chemotherapy**: Preoperative (neoadjuvant) chemotherapy to shrink the tumor and postoperative (adjuvant) chemotherapy to eliminate any remaining cancer cells.
                
                """)
    st.image("WhatsApp Image 2024-08-27 at 7.10.07 PM.jpeg", use_column_width=True)
    st.markdown("""- **Surgery**: Removal of the tumor with a margin of healthy tissue. Limb-sparing surgery is preferred, but amputation may be necessary in some cases.""")
    st.image("WhatsApp Image 2024-08-27 at 7.15.43 PM.jpeg", use_column_width=True)
    st.markdown("""- **Radiation Therapy**: Used when complete surgical resection is not possible or in cases of metastasis. It can also be used as part of the initial treatment.
    - **Targeted Therapy**:
        - **Clinical Trials**: Ongoing research into targeted therapies that specifically attack cancer cells with the EWSR1-FLI1 fusion gene.
    """, unsafe_allow_html=True)
    # st.image("E:\mallene_project\WhatsApp Image 2024-08-27 at 7.10.07 PM.jpeg", use_column_width=True)
    st.markdown("<h2>Prognosis:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Localized Disease**: Approximately 70-80% five-year survival rate with aggressive treatment.
    - **Metastatic Disease**: Significantly poorer prognosis, with a five-year survival rate of around 15-30%.
    - **Relapse**: Recurrence of the disease is a major concern and is associated with a poor prognosis.
    """, unsafe_allow_html=True)

    st.markdown("<h2>Complications:</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Treatment-Related**: Chemotherapy and radiation can lead to short- and long-term side effects, including secondary cancers, organ damage, and fertility issues.
    - **Disease-Related**: Local recurrence, metastasis, and complications from the tumor (such as fractures or neurological impairment).
    """, unsafe_allow_html=True)

    st.markdown("<h2>Follow-Up and Monitoring:</h2>", unsafe_allow_html=True)
    st.markdown("""
    Regular follow-up is crucial for early detection of recurrence. Monitoring includes physical examinations, imaging studies, and assessment of treatment side effects.
    """, unsafe_allow_html=True)

# Function to display Content2 page (Causative Protein)
def content2_page():
    st.title("Causative Protein")

    st.markdown("<h2>The EWS-FLI1 Fusion Protein:</h2>", unsafe_allow_html=True)
    st.markdown("""
    The primary causative factor in Ewing sarcoma is the EWS-FLI1 fusion protein. This abnormal protein results from a chromosomal translocation between chromosomes 11 and 22, specifically t(11;22)(q24;q12). This translocation fuses the EWSR1 gene (Ewing sarcoma breakpoint region 1) on chromosome 22 with the FLI1 gene (Friend leukemia integration 1 transcription factor) on chromosome 11.
    """, unsafe_allow_html=True)

    st.image("WhatsApp Image 2024-08-27 at 7.44.16 PM.jpeg", use_column_width=True)

# Function to display Content3 page (Sequence)
def content3_page():
    st.title("EWS-FLI1 Fusion Protein Sequence")

    st.markdown("<h2>Sequence Information:</h2>", unsafe_allow_html=True)
    st.markdown("""
   The EWS-FLI1 fusion protein is a chimeric oncoprotein that combines the N-terminal domain of the EWSR1 protein with the C-terminal DNA-binding domain of the FLI1 transcription factor.

EWSR1 Domain: The EWSR1 portion contains an RNA-binding domain and a strong transactivation domain that drives transcription.
FLI1 Domain: The FLI1 portion includes an ETS (E-twenty-six) DNA-binding domain that recognizes specific DNA sequences, leading to aberrant gene expression.
                EWS-FLI1 fusion protein sequence:

The sequence is not fixed, as different variants of the fusion gene can occur, leading to different fusion protein sequences. However, the most common variant includes the first seven exons of the EWSR1 gene fused to exons 6-9 of the FLI1 gene.
    """, unsafe_allow_html=True)
    
    # st.image("WhatsApp Image 2024-08-27 at 7.44.41 PM (3).jpeg ", use_column_width=True)
    st.image("WhatsApp Image 2024-08-27 at 7.21.51 PM.jpeg", use_column_width=True)
# Function to display Content4 page (Inhibitors)
def content4_page():
    st.title("Inhibitors of EWS-FLI1 Fusion Protein")

   
    st.markdown("""
    **TK216:**

Mechanism: A small molecule that targets and inhibits the function of the EWS-FLI1 protein by disrupting its interaction with RNA helicase A, which is essential for its oncogenic activity.
Clinical Status: TK216 has shown promise in early-phase clinical trials, particularly in patients with relapsed or refractory Ewing sarcoma.
""")
    st.image("WhatsApp Image 2024-08-27 at 7.21.51 PM.jpeg", use_column_width=True)
    st.markdown("""
**YK-4-279:**

Mechanism: An inhibitor that disrupts the interaction between EWS-FLI1 and RNA helicase A, thereby reducing the oncogenic activity of the fusion protein. YK-4-279 also induces apoptosis in Ewing sarcoma cells.
Clinical Status: YK-4-279 is still in preclinical and early clinical stages, but it has shown potential as a targeted therapy.
""")
    st.image("WhatsApp Image 2024-08-27 at 7.37.26 PM.jpeg", use_column_width=True)
    st.markdown("""
**Trabectedin:**

Mechanism: A marine-derived compound that binds to the minor groove of DNA and inhibits the transcriptional activity of the EWS-FLI1 fusion protein. Trabectedin interferes with the fusion protein's ability to regulate gene expression.
Clinical Status: Trabectedin has been used in clinical trials for patients with Ewing sarcoma, often in combination with other chemotherapy agents.

**HSP90 Inhibitors:**

Mechanism: EWS-FLI1 protein stability is partly dependent on the chaperone protein HSP90. Inhibitors of HSP90, such as ganetespib, can lead to the degradation of the EWS-FLI1 protein.
Clinical Status: HSP90 inhibitors are being investigated in preclinical models and early-phase clinical trials.

**BCL-2 Inhibitors:**

Mechanism: The EWS-FLI1 protein upregulates the expression of anti-apoptotic proteins like BCL-2. Inhibitors of BCL-2, such as venetoclax, have shown potential in sensitizing Ewing sarcoma cells to apoptosis.
Clinical Status: BCL-2 inhibitors are under investigation for use in combination with other therapies in Ewing sarcoma.
    """, unsafe_allow_html=True)
    st.image("WhatsApp Image 2024-08-27 at 7.43.07 PM.jpeg", use_column_width=True)


# Page navigation logic
def show_page(page):
    if page == "Overview":
        content1_page()
    elif page == "Causative Protein":
        content2_page()
    elif page == "Sequence":
        content3_page()
    elif page == "Inhibitors":
        content4_page()
    else:
        main_page()

# Main script
apply_custom_css()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Main Page", "Overview", "Causative Protein", "Sequence", "Inhibitors"])

if page == "Main Page":
    main_page()
else:
    show_page(page)

# Back button
# if st.sidebar.button("Back to Main Page"):
#     main_page()
