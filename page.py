!DOCTYPE html>
<!--coding by codinglab| www.codinglabweb.com-->
<html lang="en">
  <head>
     <meta charset="UTF-8"/>
     <meta htpp-equive="X-UA-compatible" content="IE=edge"/>
     <meta name="viewport" content="width, intial-scale=1.0"/>
     <link rel="stylesheet" href="style.css" rel="stylesheet" type="text/css">
     <tittle> Responsive Registration Form in HTML CSS</tittle>
  </head>
  <body>
    <section class="container">
        <header>Registration Form</header>
        <form action="#" class="form">
            <div class="input-box">
                <label> Full Name</label>
                <input type="text" placeholder="enter full name" required/>
            </div>

            <div class="input-box">
                <label> email address</address></label>
                <input type="text" placeholder="enter email address" required/>
                </div>

                <div class="column">
                    <div class="input-box">
                        <label> phone number</label>
                        <input type="text" placeholder="enter phone number"required/>
                     </div>

                     <div class="input-box">
                        <label> date of birth</label>
                        <input type="text" placeholder="enter date of birth" required/>
                     </div>
                     </div>

                     <div class="gender-box">
                            <h3>Gender</h3>
                            <div class="grnder-option">
                                <div class="gender">
                                    <input type="radio" id="check-male" name="gender" checked/>
                                    <label for="check-male"> male</label>
                                    </div>
                                    <div class="gender">
                                        <input type="radio" id="check-female" name="gender" checked />
                                        <label for="check-female"> female</label>
                                        </div>
                                        <div class="gender">
                                            <input type="radio" id="check-other" name="gender" checked/>
                                            <label for="check-other"> prefer not to say</label>
                                </div>
                                </div>
                                </div>

                                <div class="input-box address">
                                    <label>Address</label>
                                    <input type="text" placeholder="enter  street address" required/>
                                    <input type="text" placeholder="enter  street address line2" required/>
                                    <div class="column">
                                        <div class="select-box">
                                            <select>
                                                <option>country</option>
                                                <option>America</option>
                                                <option>India</option>
                                                <option>Japan</option>
                                                <option>Nepal</option>
                                            </select>

                                        </div>
                                </div>
                                    <input type="text" placeholder="enter your city " required/>
                                    <input type="text" placeholder="enter your religion" required/>
                                    <input type="text" placeholder="enter postal code" required/>
                                </div>

                                <button>submit</button>
         </form>
     </section>
  </body>
  </html>