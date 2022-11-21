'use strict';

const e = React.createElement;




// import React, {useState, useEffect} from 'react'
const AddPharmacyButton=()=> {

  const [screenStates, setScreenStates] = React.useState({
    username: "",
    email: "",
    password1: "",
    password2: "",
    pharmacy_name: "",
    address: "",
    
  })

  React.useEffect(() => {
  

   
},[])



  const handleInputs = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.value})

  }

console.log(screenStates)


const getCookie = (name)  => {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


  const AddPharmacy =() =>{
      var csrftoken = getCookie('csrftoken')
      if (screenStates.username == '' || screenStates.email == '' || screenStates.password1 == '' || screenStates.password2 == '' || screenStates.pharmacy_name == ''   ) {
        iziToast.show({message:"Lütfen bilgileri doğru giriniz", position: "topRight",
        messageColor: 'black',
        messageSize: '16',
        title: 'Başarısız',
        titleColor: 'black',
        titleSize: '16',
        maxWidth: '600',
        backgroundColor: '#f34444',
        iconColor: '#fff',
        progressBarColor: 'black',});
      }
      else{
        fetch('http://localhost:8000/add/pharmacy/react', {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"username":screenStates.username,"email":screenStates.email,"password1":screenStates.password1,"password2":screenStates.password2,"pharmacy_name":screenStates.pharmacy_name,"address":screenStates.address})

        }).then(resp => resp.json())
        
        .then(resp =>             
          (iziToast.show({
          message: resp["message"], 
          position: "topRight",
          messageColor: 'black',
          messageSize: '16',
          title: resp["type"],
          titleColor: 'black',
          titleSize: '16',
          maxWidth: '600',
          backgroundColor: resp["color"],
          iconColor: '#fff',
          progressBarColor: 'black',
          resetOnHover: true,
          transitionIn: 'flipInX',
          transitionOut: 'flipOutX',})))
         .catch(function(error){
            iziToast.show({message:"Lütfen formu doğru bir şekilde doldurun", position: "topRight",
            messageColor: 'black',
            messageSize: '16',
            title: 'Başarısız',
            titleColor: 'black',
            titleSize: '16',
            maxWidth: '600',
            backgroundColor: '#f34444',
            iconColor: '#fff',
            progressBarColor: 'black',
            resetOnHover: true,
            transitionIn: 'flipInX',
            transitionOut: 'flipOutX',});
          console.log('ERROR:', error)
        })
    
      }

  }


    return (
      <div>

        <div className="card w-50 mx-auto p-4">
              <div className="card-header py-3 mb-3">
                  <h6 className="m-0 font-weight-bold text-primary">  
                  <i className="fa fa-plus">  </i>    Eczane Ekle
                  </h6>  
              </div>
              <form method="post" action="" onSubmit={(e)=>{
                e.preventDefault()
                
                AddPharmacy()
              }}>
                
                <div className="row ">
            <div className="col-md-12 mt-2">
                <label htmlFor="id_username" className="text-md">
                    Username
                    </label>
                      
                    <input onChange={handleInputs} type="text" name="username" className="form-control form-control-user" placeholder="Username" maxLength="150" autoFocus="" required="" id="id_username" />
                     
           
            </div>
            <div className="col-md-12 mt-2">
                <label htmlFor="id_email" className="text-md">
                    Email
                    </label>
                  
                <input onChange={handleInputs} type="email" name="email" className="form-control form-control-user" placeholder="Email" max="40" required="" id="id_email" />
                 
            </div>
            <div className="col-md-12 mt-2">
                <label htmlFor="id_password1" className="text-md">
                    Password
                    </label>
                  
                <input onChange={handleInputs} type="password" name="password1" className="form-control form-control-user" placeholder="Password" required="" id="id_password1" />
                 
                </div>
                <div className="col-md-12 mt-2">
                    <label htmlFor="id_password2" className="text-md">
                        Password Confirmation
                        </label>
                      
                    <input onChange={handleInputs} type="password" name="password2" className="form-control form-control-user" placeholder="Password Confirmation" required="" id="id_password2" />
                     
    
                    </div>


                <div className="col-md-12 mt-2">
                    <label htmlFor="id_pharmacy_name" className="text-md">
                        Eczane Adı
                        </label>
                      
                    <input onChange={handleInputs} type="text" name="pharmacy_name" className="form-control form-control-user mb-2  " placeholder="Eczane Adı" required="" id="id_pharmacy_name" />
                     
    
                    </div>

                <div className="col-md-12 mt-2">
                    <label htmlFor="id_address" className="text-md">
                        Adres
                        </label>
                      
                    <textarea onChange={handleInputs} name="address" cols="10" rows="7" className="form-control form-control-user mb-2 " placeholder="Adres" maxLength="300" id="id_address"></textarea>
                     
    
                    </div>
        </div>



                      <button 
                    type="submit"
                    className="px-5 py-2 mr-3 mt-3 font-bold text-center text-white uppercase btn bg-primary"
                    id="submit_button"
                    >
                    <i className="fa fa-plus">  </i> Ekle
                    </button>
                  
              </form>
        </div>




        

        
      </div>


    );
 
}

const domContainer = document.querySelector('#add_pharmacy_container');
ReactDOM.render(<AddPharmacyButton />, domContainer);
