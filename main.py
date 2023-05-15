import lxml.etree
import tkinter as tk
from lxml import etree
from tkcalendar import DateEntry
from tkinter import messagebox

# Step 1: Parse the XML document
inventory = lxml.etree.parse('inventory.xml')

# Step 2: Create the GUI to choose the table to insert to

# create a list of table names
table_names = ["product", "supplier", "customer", "order"]

# create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("500x300")

# create a label for the dropdown menu
label = tk.Label(root, text="Choose a table:")

# create the dropdown menu
variable = tk.StringVar(root)
variable.set(table_names[0])  # set the default value
dropdown = tk.OptionMenu(root, variable, *table_names)

# create a button to show a new form
button = tk.Button(root, text="Add new record", command=lambda: show_new_form(variable.get()))

# pack the label, dropdown menu, and button into the window
label.pack()
dropdown.pack()
button.pack()


def show_suppliers_database():
    # Create a table to display the inventory data
    suppliers = inventory.xpath('/inventory/suppliers/supplier')
    # Create a new window
    window = tk.Tk()
    window.title("Suppliers Database")
    window.geometry("1000x500")

    # Add a frame to hold the widgets
    table = tk.Frame(window)
    table.pack()

    # Add table headers
    tk.Label(table, text="Name").grid(row=0, column=0)
    tk.Label(table, text="Description").grid(row=0, column=1)
    tk.Label(table, text="Category").grid(row=0, column=2)
    tk.Label(table, text="Contact Name").grid(row=0, column=3)
    tk.Label(table, text="Contact Phone").grid(row=0, column=4)
    tk.Label(table, text="Contact Email").grid(row=0, column=5)

    # Add rows for each item in the inventory
    for i, item in enumerate(suppliers):
        name = item.find('name').text
        description = item.find('description').text
        category = item.find('category').text
        contact_name = item.find('contact/name').text
        contact_phone = item.find('contact/phone').text
        contact_email = item.find('contact/email').text

        tk.Label(table, text=name).grid(row=i + 1, column=0)
        tk.Label(table, text=description).grid(row=i + 1, column=1)
        tk.Label(table, text=category).grid(row=i + 1, column=2)
        tk.Label(table, text=contact_name).grid(row=i + 1, column=3)
        tk.Label(table, text=contact_phone).grid(row=i + 1, column=4)
        tk.Label(table, text=contact_email).grid(row=i + 1, column=5)

    window.mainloop()


def show_customers_database():
    # Create a table to display the inventory data
    customers = inventory.xpath('/inventory/customers/customer')
    # Create a new window
    window = tk.Tk()
    window.title("Customers Database")
    window.geometry("1000x500")

    # Add a frame to hold the widgets
    table = tk.Frame(window)
    table.pack()

    # Add table headers
    tk.Label(table, text="Name").grid(row=0, column=0)
    tk.Label(table, text="Street").grid(row=0, column=1)
    tk.Label(table, text="City").grid(row=0, column=2)
    tk.Label(table, text="State").grid(row=0, column=3)
    tk.Label(table, text="Zip").grid(row=0, column=4)
    tk.Label(table, text="Contact Phone").grid(row=0, column=5)
    tk.Label(table, text="Contact Email").grid(row=0, column=6)

    # Add rows for each item in the inventory
    for i, item in enumerate(customers):
        name = item.find('name').text
        street = item.find('address/street').text
        city = item.find('address/city').text
        state = item.find('address/state').text
        zip = item.find('address/zip').text
        contact_phone = item.find('contact/phone').text
        contact_email = item.find('contact/email').text

        tk.Label(table, text=name).grid(row=i + 1, column=0)
        tk.Label(table, text=street).grid(row=i + 1, column=1)
        tk.Label(table, text=city).grid(row=i + 1, column=2)
        tk.Label(table, text=state).grid(row=i + 1, column=3)
        tk.Label(table, text=zip).grid(row=i + 1, column=4)
        tk.Label(table, text=contact_phone).grid(row=i + 1, column=5)
        tk.Label(table, text=contact_email).grid(row=i + 1, column=6)

    window.mainloop()


def show_products_database():
    # Create a table to display the inventory data
    products = inventory.xpath('/inventory/products/product')
    # Create a new window
    window = tk.Tk()
    window.title("Products Database")
    window.geometry("1000x500")

    # Add a frame to hold the widgets
    table = tk.Frame(window)
    table.pack()

    # Add table headers
    tk.Label(table, text="Name").grid(row=0, column=0)
    tk.Label(table, text="Description").grid(row=0, column=1)
    tk.Label(table, text="Price").grid(row=0, column=2)
    tk.Label(table, text="Category").grid(row=0, column=3)
    tk.Label(table, text="Variants Description").grid(row=0, column=4)
    tk.Label(table, text="Variants Quantity").grid(row=0, column=5)
    tk.Label(table, text="Supplier_ID").grid(row=0, column=6)

    # Add rows for each item in the inventory
    for i, item in enumerate(products):
        variants_desc_all = ""
        variants_qt_all = ""
        name = item.find('name').text
        description = item.find('description').text
        price = item.find('price').text
        category = item.find('category').text
        variants = item.find('variants')
        for j, variant in enumerate(variants):
            variants_desc = variant.find('description').text
            variants_desc_all += variants_desc + ", "
            variants_qt = variant.find('quantity').text
            variants_qt_all += variants_qt + ", "
        supplier = item.find('supplier')

        tk.Label(table, text=name).grid(row=i + 1, column=0)
        tk.Label(table, text=description).grid(row=i + 1, column=1)
        tk.Label(table, text=price).grid(row=i + 1, column=2)
        tk.Label(table, text=category).grid(row=i + 1, column=3)
        tk.Label(table, text=variants_desc_all).grid(row=i + 1, column=4)
        tk.Label(table, text=variants_qt_all).grid(row=i + 1, column=5)
        tk.Label(table, text=supplier.attrib['id']).grid(row=i + 1, column=6)

    window.mainloop()


def show_orders_database():
    # Create a table to display the inventory data
    orders = inventory.xpath('/inventory/orders/order')
    # Create a new window
    window = tk.Tk()
    window.title("Orders Database")
    window.geometry("1000x500")

    # Add a frame to hold the widgets
    table = tk.Frame(window)
    table.pack()

    # Add table headers
    tk.Label(table, text="Delivery Date").grid(row=0, column=0)
    tk.Label(table, text="Customer_ID").grid(row=0, column=1)
    tk.Label(table, text="Product_ID").grid(row=0, column=2)
    tk.Label(table, text="Variant_ID").grid(row=0, column=3)
    tk.Label(table, text="Quantity").grid(row=0, column=4)
    tk.Label(table, text="Order total").grid(row=0, column=5)

    # Add rows for each item in the inventory
    for i, item in enumerate(orders):
        variants_id = ""
        variants_qt = ""
        products_id = ""
        date = item.find('date').text
        customer = item.find('customer')
        total = item.find('total').text
        products = item.find('products')
        for j, product in enumerate(products):
            variant_id = product.attrib['variant_id']
            product_id = product.attrib['product_id']
            variant_qt = product.find('quantity').text
            variants_id += variant_id + ", "
            products_id += product_id + ", "
            variants_qt += variant_qt + ", "

        tk.Label(table, text=date).grid(row=i + 1, column=0)
        tk.Label(table, text=customer.attrib['id']).grid(row=i + 1, column=1)
        tk.Label(table, text=products_id).grid(row=i + 1, column=2)
        tk.Label(table, text=variants_id).grid(row=i + 1, column=3)
        tk.Label(table, text=variants_qt).grid(row=i + 1, column=4)
        tk.Label(table, text=total).grid(row=i + 1, column=5)

    window.mainloop()


def add_supplier(form):
    # Add labels and entry boxes for each field
    tk.Label(form, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1)

    tk.Label(form, text="Description").grid(row=1, column=0)
    description_entry = tk.Entry(form)
    description_entry.grid(row=1, column=1)

    tk.Label(form, text="Category").grid(row=2, column=0)
    category_entry = tk.Entry(form)
    category_entry.grid(row=2, column=1)

    tk.Label(form, text="Contact Name").grid(row=3, column=0)
    contact_name_entry = tk.Entry(form)
    contact_name_entry.grid(row=3, column=1)

    tk.Label(form, text="Contact Phone").grid(row=4, column=0)
    contact_phone_entry = tk.Entry(form)
    contact_phone_entry.grid(row=4, column=1)

    tk.Label(form, text="Contact Email").grid(row=5, column=0)
    contact_email_entry = tk.Entry(form)
    contact_email_entry.grid(row=5, column=1)

    # Function to add the new supplier to the inventory
    def add_supplier_to_inventory():
        # Get the data from the entry boxes
        supplier_name = name_entry.get()
        supplier_desc = description_entry.get()
        supplier_cat = category_entry.get()
        contact_name = contact_name_entry.get()
        contact_phone = contact_phone_entry.get()
        contact_email = contact_email_entry.get()

        inventory_root = inventory.getroot()

        # Find the last supplier ID to generate a new ID for the new supplier
        last_supplier = inventory_root.xpath('/inventory/suppliers/supplier[last()]')[-1]
        new_id = int(last_supplier.get('id')) + 1

        # Create the new supplier element
        new_supplier = etree.Element('supplier', id=str(new_id))

        # Create the child elements and add them to the new supplier
        name = etree.Element('name')
        name.text = supplier_name
        new_supplier.append(name)

        description = etree.Element('description')
        description.text = supplier_desc
        new_supplier.append(description)

        category = etree.Element('category')
        category.text = supplier_cat
        new_supplier.append(category)

        contact = etree.Element('contact')
        contact_name_element = etree.Element('name')
        contact_name_element.text = contact_name
        contact.append(contact_name_element)
        contact_phone_element = etree.Element('phone')
        contact_phone_element.text = contact_phone
        contact.append(contact_phone_element)
        contact_email_element = etree.Element('email')
        contact_email_element.text = contact_email
        contact.append(contact_email_element)
        new_supplier.append(contact)

        # Add the new supplier to the suppliers element
        suppliers_element = inventory_root.find('suppliers')
        suppliers_element.append(new_supplier)

        # Write the modified XML back to file
        inventory.write('inventory.xml', pretty_print=True)

        # Close the "Add Supplier" window
        form.destroy()

        show_suppliers_database()

    submit_button = tk.Button(form, text="Add Supplier", command=add_supplier_to_inventory)
    submit_button.grid(row=6, column=0, columnspan=2)


def add_product(form):
    # Add labels and entry boxes for each field
    tk.Label(form, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1)

    tk.Label(form, text="Description").grid(row=1, column=0)
    description_entry = tk.Entry(form)
    description_entry.grid(row=1, column=1)

    tk.Label(form, text="Price").grid(row=2, column=0)
    price_entry = tk.Spinbox(form, from_=0, to=10000, width=10)
    price_entry.grid(row=2, column=1)

    tk.Label(form, text="Category").grid(row=3, column=0)
    category_entry = tk.Entry(form)
    category_entry.grid(row=3, column=1)

    # find existing supplier names from the database to put them in the dropdown
    tk.Label(form, text="Supplier").grid(row=4, column=0)
    suppliers = inventory.findall('.//suppliers/supplier/name')
    supplier_choices = [supplier.text for supplier in suppliers]
    supplier_var = tk.StringVar(form)
    supplier_var.set(supplier_choices[0])
    supplier_dropdown = tk.OptionMenu(form, supplier_var, *supplier_choices)
    supplier_dropdown.grid(row=4, column=1)

    tk.Label(form, text="Number of variants").grid(row=5, column=0)
    variants_entry = tk.Spinbox(form, from_=0, to=100, width=10)
    variants_entry.grid(row=5, column=1)
    variants_desc = []
    variants_qt = []

    def show_variant_entries():
        # Get the number of variants from the entry box
        num_variants = int(variants_entry.get())

        # Create a frame to hold the variant entry fields
        variant_frame = tk.Frame(form)
        tk.Label(variant_frame, text="Description").grid(row=5, column=1)
        tk.Label(variant_frame, text="Quantity").grid(row=5, column=2)
        variant_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Create labels and entries for each variant
        for i in range(num_variants):
            variant_label = tk.Label(variant_frame, text=f'Variant {i + 1}:')
            variant_label.grid(row=i, column=0, sticky='e')
            variant_desc_entry = tk.Entry(variant_frame)
            variant_desc_entry.grid(row=i, column=1)
            variants_desc.append(variant_desc_entry)
            variant_qty_entry = tk.Spinbox(variant_frame, from_=0, to=100, width=10)
            variant_qty_entry.grid(row=i, column=2)
            variants_qt.append(variant_qty_entry)

        variants_button.destroy()
        submit_button = tk.Button(form, text="Add Product", command=add_product_to_inventory)
        submit_button.grid(row=12, column=0, columnspan=2)

    variants_button = tk.Button(form, text='Enter', command=show_variant_entries)
    variants_button.grid(row=11, column=0, columnspan=2)

    def add_product_to_inventory():
        # Get the data from the entry boxes
        product_name = name_entry.get()
        product_description = description_entry.get()
        product_price = price_entry.get()
        product_category = category_entry.get()
        product_supplier = supplier_var.get()
        variants_num = int(variants_entry.get())

        inventory_root = inventory.getroot()

        # Find the last product ID to generate a new ID for the new product
        last_product = inventory_root.xpath('/inventory/products/product[last()]')[-1]
        new_id = int(last_product.get('id')) + 1

        # Create the new product element
        new_product = etree.Element('product', id=str(new_id))

        # Create the child elements and add them to the new product
        name = etree.Element('name')
        name.text = product_name
        new_product.append(name)

        description = etree.Element('description')
        description.text = product_description
        new_product.append(description)

        price = etree.Element('price')
        price.text = product_price
        new_product.append(price)

        category = etree.Element('category')
        category.text = product_category
        new_product.append(category)

        variants_elem = etree.Element('variants')
        for i in range(variants_num):
            variant_elem = etree.Element('variant')
            variant_elem.set('id', str(i + 1))
            desc_elem = etree.Element('description')
            desc_elem.text = variants_desc[i].get()
            variant_elem.append(desc_elem)
            qty_elem = etree.Element('quantity')
            qty_elem.text = variants_qt[i].get()
            variant_elem.append(qty_elem)
            variants_elem.append(variant_elem)

        new_product.append(variants_elem)

        supplier = inventory.find(f".//suppliers/supplier[name='{product_supplier}']")
        supplier_elem = etree.Element('supplier')
        supplier_elem.set('id', str(supplier.attrib['id']))
        new_product.append(supplier_elem)

        # Add the new product to the products element
        products_element = inventory_root.find('products')
        products_element.append(new_product)

        # Write the modified XML back to file
        inventory.write('inventory.xml', pretty_print=True)

        # Close the "Add Customer" window
        form.destroy()

        show_products_database()


def add_customer(form):
    # Add labels and entry boxes for each field
    tk.Label(form, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1)

    tk.Label(form, text="Street").grid(row=1, column=0)
    street_entry = tk.Entry(form)
    street_entry.grid(row=1, column=1)

    tk.Label(form, text="City").grid(row=2, column=0)
    city_entry = tk.Entry(form)
    city_entry.grid(row=2, column=1)

    tk.Label(form, text="State").grid(row=3, column=0)
    state_entry = tk.Entry(form)
    state_entry.grid(row=3, column=1)

    tk.Label(form, text="Zip").grid(row=4, column=0)
    zip_entry = tk.Entry(form)
    zip_entry.grid(row=4, column=1)

    tk.Label(form, text="Contact Phone").grid(row=5, column=0)
    contact_phone_entry = tk.Entry(form)
    contact_phone_entry.grid(row=5, column=1)

    tk.Label(form, text="Contact Email").grid(row=6, column=0)
    contact_email_entry = tk.Entry(form)
    contact_email_entry.grid(row=6, column=1)

    # Function to add the new customer to the inventory
    def add_customer_to_inventory():
        # Get the data from the entry boxes
        customer_name = name_entry.get()
        customer_street = street_entry.get()
        customer_city = city_entry.get()
        customer_state = state_entry.get()
        customer_zip = zip_entry.get()
        contact_phone = contact_phone_entry.get()
        contact_email = contact_email_entry.get()

        inventory_root = inventory.getroot()

        # Find the last customer ID to generate a new ID for the new customer
        last_customer = inventory_root.xpath('/inventory/customers/customer[last()]')[-1]
        new_id = int(last_customer.get('id')) + 1

        # Create the new customer element
        new_customer = etree.Element('customer', id=str(new_id))

        # Create the child elements and add them to the new customer
        name = etree.Element('name')
        name.text = customer_name
        new_customer.append(name)

        address = etree.Element('address')
        street = etree.Element('street')
        street.text = customer_street
        address.append(street)
        city = etree.Element('city')
        city.text = customer_city
        address.append(city)
        state = etree.Element('state')
        state.text = customer_state
        address.append(state)
        zip = etree.Element('zip')
        zip.text = customer_zip
        address.append(zip)
        new_customer.append(address)

        contact = etree.Element('contact')
        contact_phone_element = etree.Element('phone')
        contact_phone_element.text = contact_phone
        contact.append(contact_phone_element)
        contact_email_element = etree.Element('email')
        contact_email_element.text = contact_email
        contact.append(contact_email_element)
        new_customer.append(contact)

        # Add the new supplier to the suppliers element
        customers_element = inventory_root.find('customers')
        customers_element.append(new_customer)

        # Write the modified XML back to file
        inventory.write('inventory.xml', pretty_print=True)

        # Close the "Add Customer" window
        form.destroy()
        show_customers_database()

    submit_button = tk.Button(form, text="Add Customer", command=add_customer_to_inventory)
    submit_button.grid(row=7, column=0, columnspan=2)


def add_order(form):
    # Add labels and entry boxes for each field
    tk.Label(form, text="Delivery Date").grid(row=0, column=0)
    cal = DateEntry(form, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.grid(row=0, column=1)

    tk.Label(form, text="Customer").grid(row=1, column=0)
    customers = inventory.findall('.//customers/customer/name')
    customer_choices = [customer.text for customer in customers]
    customer_var = tk.StringVar(form)
    customer_var.set(customer_choices[0])
    customer_dropdown = tk.OptionMenu(form, customer_var, *customer_choices)
    customer_dropdown.grid(row=1, column=1)

    tk.Label(form, text="Number of Products").grid(row=2, column=0)
    products_entry = tk.Spinbox(form, from_=0, to=100, width=10)
    products_entry.grid(row=2, column=1)
    product_name = []
    product_variant = []
    product_quantity = []

    def show_product_entries():
        # Get the number of products from the entry box
        num_products = int(products_entry.get())

        # Create a frame to hold the product entry fields
        products_frame = tk.Frame(form)
        products_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Create labels and entries for each product
        for i in range(num_products):
            tk.Label(products_frame, text=f'Product {i + 1} Name:').grid(row=i, column=0, sticky='e')
            products = inventory.findall('.//products/product/name')
            product_choices = [product.text for product in products]
            product_var = tk.StringVar(form)
            product_var.set(product_choices[0])
            product_dropdown = tk.OptionMenu(products_frame, product_var, *product_choices)
            product_dropdown.grid(row=i, column=1)
            product_name.append(product_var)

            products_button.destroy()

        def show_variants_entries():
            for j in range(num_products):
                variant_desc = []
                tk.Label(products_frame, text=f'Product {j + 1} Quantity:').grid(row=j, column=4, sticky='e')
                variant_qty_entry = tk.Spinbox(products_frame, from_=0, to=100, width=10)
                variant_qty_entry.grid(row=j, column=5)
                product_quantity.append(variant_qty_entry)

                tk.Label(products_frame, text=f'Product {j + 1} Variant:').grid(row=j, column=6, sticky='e')
                product = inventory.xpath('/inventory/products/product')
                for m, item in enumerate(product):
                    name = item.find('name').text
                    if name == product_name[j].get():
                        variants = item.find('variants')
                        for n, variant in enumerate(variants):
                            variant_desc.append(variant.find('description').text)

                variants_choices = [variant for variant in variant_desc]
                variant_var = tk.StringVar(form)
                variant_var.set(variants_choices[0])
                variants_dropdown = tk.OptionMenu(products_frame, variant_var, *variants_choices)
                variants_dropdown.grid(row=j, column=7)
                product_variant.append(variant_var)

            variants_button.destroy()
            submit_button = tk.Button(form, text="Add Order", command=add_order_to_inventory)
            submit_button.grid(row=12, column=0, columnspan=2)

        variants_button = tk.Button(products_frame, text='Enter', command=show_variants_entries)
        variants_button.grid(row=num_products + 1, column=2, columnspan=2)

    products_button = tk.Button(form, text='Enter', command=show_product_entries)
    products_button.grid(row=11, column=0, columnspan=2)

    def add_order_to_inventory():
        # Get the data from the entry boxes
        delivery_date = cal.get()
        customer_order = customer_var.get()
        products_num = int(products_entry.get())

        inventory_root = inventory.getroot()

        # Find the last order ID to generate a new ID for the new order
        last_order = inventory_root.xpath('/inventory/orders/order[last()]')[-1]
        new_id = int(last_order.get('id')) + 1

        # Create the new order element
        new_order = etree.Element('order', id=str(new_id))

        # Create the child elements and add them to the new order
        date = etree.Element('date')
        date.text = delivery_date
        new_order.append(date)

        products_elem = etree.Element('products')
        order_total = 0
        for i in range(products_num):
            product_elem = etree.Element('product')
            product_node = inventory.xpath(f'//product[name="{product_name[i].get()}"]')[0]
            order_total += int(int(product_node.find('price').text) * int(product_quantity[i].get()))
            product_elem.set('product_id', product_node.attrib['id'])
            variant_elem = product_node.xpath(f"variants/variant[description='{product_variant[i].get()}']")[0]
            variant_id = variant_elem.get('id')
            variant_quantity = variant_elem.find('quantity')
            variant_quantity.text = str(int(variant_quantity.text) - int(product_quantity[i].get()))
            product_elem.set('variant_id', variant_id)
            qty_elem = etree.Element('quantity')
            qty_elem.text = product_quantity[i].get()
            product_elem.append(qty_elem)
            products_elem.append(product_elem)

        new_order.append(products_elem)

        customer = inventory.find(f".//customers/customer[name='{customer_order}']")
        customer_elem = etree.Element('customer')
        customer_elem.set('id', str(customer.attrib['id']))
        new_order.append(customer_elem)

        total = etree.Element('total')
        total.text = str(order_total)
        new_order.append(total)

        # Add the new order to the orders element
        orders_element = inventory_root.find('orders')
        orders_element.append(new_order)

        # Write the modified XML back to file
        inventory.write('inventory.xml', pretty_print=True)

        form.withdraw()  # Hide the main window

        messagebox.showinfo("Order Total", str(order_total))

        # Close the "Add Customer" window
        form.destroy()
        show_orders_database()
        show_products_database()


# function to create and display a new form based on the selected table
def show_new_form(selected_table):
    # create a new form window
    form = tk.Toplevel(root)
    form.geometry("500x300")

    # set the title of the form window based on the selected table
    form.title(f"Add new record to {selected_table} table")

    # create widgets for the form (e.g. labels, entry fields, buttons)
    if selected_table == "supplier":
        add_supplier(form)
    if selected_table == "product":
        add_product(form)
    if selected_table == "customer":
        add_customer(form)
    if selected_table == "order":
        add_order(form)


# run the main event loop
root.mainloop()
# show_customers_database()
# show_products_database()
# show_orders_database()
# show_suppliers_database()
