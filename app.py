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
    st.title("Product Showcase")

    # Product Details
    st.header("Product Name: Awesome Widget")

    # Description of the product
    st.write("""
        This is an awesome widget that helps with many tasks.
        It's designed to make your life easier and more productive.
        * High-quality material
        * Durable and long-lasting
        * Available in multiple colors
        * Affordable pricing
    """)

    # Pricing Information
    st.subheader("Price: $99.99")

    # Button to simulate adding to cart
    if st.button("Add to Cart"):
        st.write("Added to Cart!")

    # Customer Reviews
    st.header("Customer Reviews")
    st.write("""
        * ⭐⭐⭐⭐⭐ - "This widget is amazing! It made my tasks so much easier."
        * ⭐⭐⭐⭐ - "Great quality, but could be improved in some areas."
        * ⭐⭐⭐⭐⭐ - "Love it! Totally worth the price."
    """)

    # About Page

elif selection == "About":
 st.header("About This Blog")
 st.markdown("![Alt Text](https://netsurfdirect.com/Content/products/821.jpg)")
 st.write("This blog is created using Streamlit. It's simple, interactive, and fun!")

      # Contact Page
elif selection == "Contact":
 st.header("Contact Me")
 st.subheader("PHONE:9440230314")
 st.write("Feel free to reach out via email or social media!")
 st.text_input("Your Email")
 st.text_area("Message")
 if st.button("Send"):
     st.success("Message sent successfully!")



