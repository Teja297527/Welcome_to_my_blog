import streamlit as st

# Set the title of the blog
st.title("WELCOME TO OUR BLOG!")

# Add a sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home","Product", "About", "Contact"]
selection = st.sidebar.radio("Go to", pages)

    # Home Page
if selection == "Home":
    st.header("A Healthy Cow Gives Healthy Milk...")
    st.markdown(
        "![Alt Text](https://d147a5vd7kzml6.cloudfront.net/img/cowsignals_com/2614/2560x1440/resize:fixed/cowsignals_2560px.jpg)")
    st.write("The cow should be healthy to give healthy milk for another people."
             "so the product is useful for animals to give that strength to animal."
             "it is a useful product for cleaning of stomach of animals and give healthy nutrients.")

    # Product Page

if selection == "Product":

    # Add a product image (use an actual image URL or local file path)
    st.markdown("![Alt Text](https://netsurfdirect.com/Content/products/821.jpg)")

      # Title of the page
    st.title("NETSURF'S BIOFIT CATTLE FEED")

    # Product Details
    st.header("Product Name: PET VET")

    # Description of the product
    st.write("""
        It is used for animals like Cow,Buffalo,Horse,Sheep,Dog,etc.
        It will increase the efficiency of milk production.
        * RUMEN Function and feeding stability will be optimised.
        * It will improve Count of nutrients,SNF and Fats in the milk.
        * It will improve taking Powdered items. 
        * It is used for the porposes of different animals.
    """)

    # Pricing Information
    st.subheader("Price:1000/-")

    # Button to simulate adding to cart
    if st.button("BUY NOW"):
        st.write("PLEASE CONTACT TO 9440230314")

    # Customer Reviews
    st.header("Customer Reviews")
    st.write("""
        * ⭐⭐⭐⭐⭐ - "This is a amazing product.And iam using for long years."
        * ⭐⭐⭐⭐⭐ - "Excellent product.Results are very good after using this product."
        * ⭐⭐⭐⭐⭐ - "Love it! This product was stolen my heart with this results."
        * ⭐⭐⭐⭐⭐ - "This product can be used for all types of animals.We can try this one."
    """)


# About Page

elif selection == "About":
 st.header("About This Blog")
 st.markdown("![Alt Text](https://5.imimg.com/data5/ANDROID/Default/2023/12/369790637/JC/XD/AP/64293832/product-jpeg-500x500.jpg)")
 st.write("""
     * It is also available for animals like Sheep,Goat,and also for Poultry.
     * It will be useful for good health of a growing baby in animals.
     * It improve weight of animals and also immunity of a animal.
     * It will decrease the rate of death of a animal.
     
     This product is useful for all types of problems of animals.
     Which were faced by animals.It some type of nutrients which recover the problem.
     So, it can cure the diseases of animals and also boost in production.
     It is a very useful product for animals........""")


 st.write("......THANK YOU.......")


      # Contact Page
elif selection == "Contact":
 st.header("Contact Me")
 st.subheader("PHONE:9440230314")
 st.subheader("MAIL:nagabushanamvanarasa@gmail.com")
 st.write("Mail to this Gmail..")  
 st.write("Feel free to reach out via email or social media!")
 st.text_input("Your Email")
 st.text_area("Message")
 if st.button("Send"):
     st.success("Message sent successfully!")



