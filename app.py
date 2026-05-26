import streamlit as st
from src.workflow import Workflow

st.set_page_config(
    page_title="AI Developer Tools Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Developer Tools Research Agent")

st.markdown("""
Research developer tools, APIs, databases, frameworks,
and AI products automatically using AI agents.
""")

query = st.text_input(
    "Enter your research query",
    placeholder="Example: best backend as a service tools"
)

if st.button("Research Tools"):
    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        with st.spinner("Researching tools..."):
            try:
                workflow = Workflow()
                result = workflow.run(query)

                st.success("Research Completed!")

                # Recommendations
                st.subheader("📌 AI Recommendations")
                st.write(result.analysis)

                # Companies
                st.subheader("🔬 Tool Analysis")

                for company in result.companies:
                    with st.expander(f"🚀 {company.name}"):

                        st.write("### Description")
                        st.write(company.description)

                        st.write("### Website")
                        st.write(company.website)

                        st.write("### Pricing")
                        st.write(company.pricing_model)

                        st.write("### Open Source")
                        st.write(company.is_open_source)

                        st.write("### API Available")
                        st.write(company.api_available)

                        st.write("### Tech Stack")
                        st.write(", ".join(company.tech_stack))

                        st.write("### Language Support")
                        st.write(", ".join(company.language_support))

                        st.write("### Integrations")
                        st.write(", ".join(company.integration_capabilities))

            except Exception as e:
                st.error(f"Error: {str(e)}")