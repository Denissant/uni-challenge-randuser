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


# contains the first part of html code
html_string = """
    <html>
        <body style="background-color:FFFAED">
        <style>
            #boxstyle {
                position: relative;
                display: inline-block;
                margin;left:120px;
                padding: 10px;
                background-color:D7FCD7;
                width: 350px;
                height: 300px;
                border:5px solid white;
            }
            
            .namestyle {
                position: static;
                font-family: Verdana;
                font-size: 25px;
                text-align:left;
                right: 10px
            }
        
            .infostyle {
                position: left;
                font-family: Courier;
                text-align: left;
                left: 10px
            }
        
            .imagestyle {
                display: block;
                align: left;
                border-radius: 15px;
            }
        </style>
"""
