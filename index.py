body{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding: 20px;
    background:rgb(130,106,251)
} 
.container{
   position: relative;
   max-width: 700px;
   width: 100%;
   background: #fff;
   padding: 25px;
   border-radius: 8px;
   box-shadow: 0 0 15px  rgba(0,0, 0, 0);
}
.container header{
    font-size:  1.5rem;
    color: #333;
    font-weight: 500;
    text-align: center;
 }
 .container .form{
    margin-top: 30px;
 }
 .form .input-box{
    width: 100%;
    margin-top: 20px;
 }
 .input-box label {
    color: #333;
 }
 .form :where(.input-box input, .select-box) {
    position: relative;
    height: 50px;
    width: 100%;
    outline: none;
    font-size: 1rem;
    color: #707070;
    margin-top: 8px;
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 0 15px;
 }
 .form.column{
    display:flex;
    column-gap: 15px;
 }
 .form.gender-box{
    margin-top: 20px;
 }
 .gender-box h3{
    color: #333;
    font-size: 1rem;
    font-weight: 400;
    margin-bottom: 8px;
 }
 .form :where(.gender-option,.gender){
    display: flex;
    align-items: center;
    column-gap: 50px;
    flex-wrap: wrap;
 }
 .form.gender{
    column-gap: 5px; 
 }
.form :where(.gender input, .gender label ){
    cursor: pointer;
}
.address:where(input,.select-box){
    margin-top: 15px;
}
.select-box select{
    height: 100%;
    width: 100%;
    outline:none ;
    border: none;
    color: #707070;
    font-size: 1rem;
}
.form button{
    height: 55px;
    width: 10;
    color: #fff;
    font-size: 1rem;
    border: none;
    margin-top: 30px;
    cursor: pointer;
    border-radius: 6px;
    font-weight: 400;
    transition: all 0.2s ease;
    background-color: rgb(130,106,251);
}
.form button:hover{
background-color: rgb(8,106,251);
}
/*Responsive */
 @media screen and (max-width:500px){
    .form.column {
        flex-wrap: wrap;
    }
    .form :where(.gender-option,.gender){
        row-gap: 15px;
    }

    

    }