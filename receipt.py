# Import smtplib, MIMEMultipart, MIMEText, and getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
 
# Create a MIMEMultipart object
msg = MIMEMultipart()
 
# Set the sender, recipient, subject, and headers
sender = "testtanuson@gmail.com"
recipient = "anucha140613@gmail.com"
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = "Test HTML Email"
msg['X-Mailer'] = "Python"
 
# Create a MIMEText object for plain text
plain_text = "Hi,\nThis is a test email.\nHere is the link you wanted:\nhttps://www.python.org"
part1 = MIMEText(plain_text, 'plain')
# Create a MIMEText object for HTML
html_text = """
<html>
<head>
    <title>Receipt Page</title>
    <style>    
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&display=swap');

    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #fff;
        color: #000;
        font-family: 'Inter', sans-serif;
    }

.receipt {
    border: 2px solid #000;
    max-width: 1200px;
    margin: 0 auto;
    padding-top: 20px;
    height: 100%;
}

.header {
    text-align: center;
    font-size: 40px;
    margin-bottom: 10px;
    color: #000;
}

.semi-header {
    text-align: center;
    font-size: 25px;
    margin-bottom: 10px;
    color: #000;
}

.semisub-header {
    text-align: center;
    font-size: 20px;
    font-weight: 10px;
    margin-bottom: 10px;
    color: #000;
}

.order-id {
    text-align: center;
    font-size: 15px;
    font-weight: 10px;
    color: #626262;
    margin-bottom: 10px;
}
.text-orderhead{
    display: flex;
    justify-content: space-between;
    padding-right: 10px;
    padding-left: 10px;
}
.order-head {
    background-color: black;
    width: 100%;
    height: 50px;
    color: white;
}

.item-head{
    padding: 2px 15px 2px 15px;
    font-weight: 700;
}

.shop-name{
    font-size: 20px;
}

.gray-line{
    width: 95%;
    height: 1px;
    background-color: #B0B0B0;
    margin: 0 auto;
    margin-bottom: 20px;
}

.imgs{
    width: 120px;
    padding-top: 20px;
    padding-bottom: 20px;
    position: relative;
    left: 10px;
}

.item-info{
    display: grid;
    grid-template-columns: 140px auto 250px auto 250px;
}

.item-name{
    font-weight: 700;
}

.item-tags{
    display: flex;
    position: relative;
    bottom: 10px;
}
.tag{
    background-color: black;
    color: white;
    border-radius: 20px;
    font-size: 5px;
    font-weight: 600;
    padding: 5px 10px 5px 10px;
    margin-right: 10px;
}
.price-per-item{
    text-align: center;
    position: relative;
    top: 30%;
}
.price-per{
    font-size: 19px;
    font-weight: 700;
}
.price-perinfo{
    font-size: 12px;
    color: #989898;
}
.size-amount{
    position: relative;
    top: 20px;
    display: flex;
    justify-content: center;
}
.size-icon{
    width: 17px;
    height: 17px;
    background-color: black;
    color: white;
    font-size: 12px;
    font-weight: 800;
    text-align: center;
    border-radius: 3px;
    padding: 3px;
    margin-bottom: 5px;
    margin-right: 40px;
}
.amount{
    font-size: 15px;
}
.item-sub{
    position: relative;
    top: 20%;
    text-align: center;
}
.item-allamount{
     font-weight: 500;
     font-size: 15px;
     color: 6C6C6C;
}
.item-allprice{
    font-weight: 700;
     font-size: 25px;
     color: black;
}
.item-allprice-notetzero{
    font-weight: 400;
    font-size: 12px;
    color: #989898;
}
.sub-price{
    display: grid;
    grid-template-columns: 80px auto 150px 250px 100px 210px;
    padding: 20px;
    align-items: center;
}
.product-price{
    text-align: center;
    font-size: 12px;
}
.carbon-credit-price{
    text-align: center;
}
.sub-cc{
    font-size: 12px;
}
.per-cc{
    font-size: 10px;
}
.order-total{
    text-align: center;
    font-size: 15px;
}
.total-price{
    text-align: center;
    color: #FB6E4F;
    font-weight: 800;
    font-size: 25px;
}
    </style>
</head>
<body>
    <div class="receipt">
        <div class="header">
            Thank you.
        </div>
        <div class="semi-header">
            Hi Username
        </div>
        <div class="semisub-header">
            Thank you for Order from us!
        </div>
        <div class="order-id">
           Order Id : 3432414131
        </div>
        <div class="order-id">
            Order date : 25/07/2023
         </div>

        <div class="order-info">
            <div class="order-head">
                <div class="text-orderhead">
                    <p class="Description">Description:</p>
                    <p class="Price">Price:</p>
                </div>
            </div>

            <div class="items">
                <div class="item-head">
                    <div class="shop-name">
                        <p>Shop Name</p>
                    </div>
                </div>

                <div class="gray-line"></div>

                <div class="item-info">
                    <div class="item-pic">
                        <img src="{image_url_or_path}" alt="" class="imgs">
                    </div>

                    <div class="item-detail">
                        <div class="item-name">
                            <p>Product Name</p>
                        </div>
                        <div class="item-tags">
                            <div class="tag">
                                Oversized
                            </div>
                            <div class="tag">
                                V-neck
                            </div>
                            <div class="tag">
                                Street Fashion
                            </div>
                        </div>
                    </div>

                    <div class="price-per-item">
                        <div class="price-per">
                            300-450 THB
                        </div>
                        <div class="price-perinfo">
                            270-420 THB ( Not Net-Zero )
                        </div>
                    </div>

                    <div class="item-amount">
                        <div class="size-amount">
                            <div class="size-icon">
                                S
                            </div>
                            <div class="amount">
                                20
                            </div>
                        </div>
                        <div class="size-amount">
                            <div class="size-icon">
                                M
                            </div>
                            <div class="amount">
                                20
                            </div>
                        </div>
                        <div class="size-amount">
                            <div class="size-icon">
                                L
                            </div>
                            <div class="amount">
                                20
                            </div>
                        </div>
                    </div>

                    <div class="item-sub">
                        <div class="item-allamount">
                            100 Item
                        </div>
                        <div class="item-allprice">
                            4,250 THB
                        </div>
                        <div class="item-allprice-notetzero">
                            3,950 THB ( Not Net-Zero )
                        </div>
                    </div>

                </div>

                <div class="gray-line"></div>

                <div class="items">
                    <div class="item-head">
                        <div class="shop-name">
                            <p>Shop Name</p>
                        </div>
                    </div>
    
                    <div class="gray-line"></div>
    
                    <div class="item-info">
                        <div class="item-pic">
                            <img src="image/istockphoto-1151955708-170667a.jpg" alt="" class="imgs">
                        </div>
    
                        <div class="item-detail">
                            <div class="item-name">
                                <p>Product Name</p>
                            </div>
                            <div class="item-tags">
                                <div class="tag">
                                    Oversized
                                </div>
                                <div class="tag">
                                    V-neck
                                </div>
                                <div class="tag">
                                    Street Fashion
                                </div>
                            </div>
                        </div>
    
                        <div class="price-per-item">
                            <div class="price-per">
                                300-450 THB
                            </div>
                            <div class="price-perinfo">
                                270-420 THB ( Not Net-Zero )
                            </div>
                        </div>
    
                        <div class="item-amount">
                            <div class="size-amount">
                                <div class="size-icon">
                                    S
                                </div>
                                <div class="amount">
                                    20
                                </div>
                            </div>
                            <div class="size-amount">
                                <div class="size-icon">
                                    M
                                </div>
                                <div class="amount">
                                    20
                                </div>
                            </div>
                            <div class="size-amount">
                                <div class="size-icon">
                                    L
                                </div>
                                <div class="amount">
                                    20
                                </div>
                            </div>
                        </div>
    
                        <div class="item-sub">
                            <div class="item-allamount">
                                100 Item
                            </div>
                            <div class="item-allprice">
                                4,250 THB
                            </div>
                            <div class="item-allprice-notetzero">
                                3,950 THB ( Not Net-Zero )
                            </div>
                        </div>
    
                    </div>
    
                    <div class="gray-line"></div>

                <div class="sub-price">
                    <div></div>
                    <div></div>
                    <div class="product-price">
                        Product Price : 3,950 THB
                    </div>
                    <div class="carbon-credit-price">
                        <div class="sub-cc">
                            Carbon Credit support : 300 THB
                        </div>
                        <div class="per-cc">
                            Carbon Credit support : 30 THB / item 
                        </div>
                    </div>
                    <div class="order-total">
                        Order total:
                    </div>
                    <div class="total-price">
                        4,250 THB
                    </div>
                </div>
            </div>

        </div>

    </div>
</body>
</html>
"""
part2 = MIMEText(html_text, 'html')
 
# Attach both parts to the message
msg.attach(part1)
msg.attach(part2)
 
# Create an SMTP object
smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Start TLS encryption
smtp.starttls()
 
# Log in with your Gmail username and password
username = sender
# password = getpass("Enter your password: ")
password = "ahesmzrdtxawnlxs"
smtp.login(username, password)
 
# Send the email message
smtp.sendmail(sender, recipient, msg.as_string())
 
# Close the SMTP connection
smtp.quit()