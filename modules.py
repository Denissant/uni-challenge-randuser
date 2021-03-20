import requests


def rand_user(count):
    result = requests.get(f'https://randomuser.me/api/?results={count}&inc=email,name,dob,cell,picture&noinfo')
    return result.json()


def create_html_string(users, html_string):
    for user in users:
        html_string += f"""
            <div id="boxstyle">
                <img src={user['picture']['large']} class="imagestyle">
                <p class="namestyle">{user['name']['first']} {user['name']['last']}</p>
                <p class="infostyle"> Age: {user['dob']['age']}</p>
                <p class="infostyle"> Email: {user['email']}</p>
                <p class="infostyle"> Phone: {user['cell']}</p>
            </div>
    """
    html_string += "</body></html>"
    return html_string
# 1B7AD7

# contains the first part of html code
html_string = """
    <html>
        <body style="background-color:FFF2F1">
        <style>
            #boxstyle {
                position: relative;
                display: inline-block;
                margin;left:80px;
                margin;top:60px;
                margin: 20px;
                padding: 10px;
                border-radius: 100px;
                background-color:D23E2F;
                width: 350px;
                height: 370px;
                border: 1px solid white;
                box-shadow: 3px 10px 20px #5E241E;
            }
            
            .namestyle {
                position: static;
                font-family: Verdana;
                font-size: 26px;
                font-weight:bold;
                text-align: center;
                white-space: nowrap;
                overflow: hidden;
                right: 10px;
                color: white
            }
        
            .infostyle {
                position: left;
                font-family: Verdana;
                font-size: 17px;
                text-align: center;
                white-space: nowrap;
                overflow: hidden;
                left: 10px;
                color: white
            }
        
            .imagestyle {
                display: block;
                align: center;
                border-radius: 100px;
                border: 5px solid white;
                margin-left: auto;
                margin-right: auto;
                width: 40%;
            }
        </style>
"""
