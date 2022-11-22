'use strict';

const e = React.createElement;



const AddPharmacyButton=()=> {

  // const [screenStates, setScreenStates] = React.useState({
  //   username: "",
  //   email: "",
  //   password1: "",
  //   password2: "",
  //   pharmacy_name: "",
  //   address: "",
    
  // })

  const [username, setUsername] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [password1, setPassword] = React.useState("");
  const [password2, setPassword2] = React.useState("");
  const [pharmacy_name, setPharmacyName] = React.useState("");
  const [address, setAdress] = React.useState("");


  React.useEffect(() => {

},[])

const handlePharmacy = (e) =>{
  setPharmacyName(e.target.value)
}

  const handleAdress = (e) =>{
    setAdress(e.target.value)
  }
  const handleUsername = (e) =>{
    setUsername(e.target.value)
  }
  const handleEmail = (e) =>{
    setEmail(e.target.value)
  }
  const handlePassword1 = (e) =>{
    setPassword(e.target.value)
  }
  const handlePassword2 = (e) =>{
    setPassword2(e.target.value)
  }

  const clearState = () =>{
    setPassword2("")
    setPassword("")
    setEmail("")
    setUsername("")
    setAdress("")
    setPharmacyName("")

  }


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
      if (username == '' || email == '' || password1 == '' || password2 == '' || pharmacy_name == ''   ) {
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
            body:JSON.stringify({"username":username,"email":email,"password1":password1,"password2":password2,"pharmacy_name":pharmacy_name,"address":address})

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
          .then(resp => clearState())
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
                      
                    <input onChange={handleUsername} value={username} type="text" name="username" className="form-control form-control-user" placeholder="Username" maxLength="150" autoFocus="" required="" id="id_username" />
                     
           
            </div>
            <div className="col-md-12 mt-2">
                <label htmlFor="id_email" className="text-md">
                    Email
                    </label>
                  
                <input onChange={handleEmail} value={email} type="email" name="email" className="form-control form-control-user" placeholder="Email" max="40" required="" id="id_email" />
                 
            </div>
            <div className="col-md-12 mt-2">
                <label htmlFor="id_password1" className="text-md">
                    Password
                    </label>
                  
                <input onChange={handlePassword1} value={password1} type="password" name="password1" className="form-control form-control-user" placeholder="Password" required="" id="id_password1" />
                 
                </div>
                <div className="col-md-12 mt-2">
                    <label htmlFor="id_password2" className="text-md">
                        Password Confirmation
                        </label>
                      
                    <input onChange={handlePassword2} value={password2} type="password" name="password2" className="form-control form-control-user" placeholder="Password Confirmation" required="" id="id_password2" />
                     
    
                    </div>


                <div className="col-md-12 mt-2">
                    <label htmlFor="id_pharmacy_name" className="text-md">
                        Eczane Adı
                        </label>
                      
                    <input onChange={handlePharmacy} value={pharmacy_name} type="text" name="pharmacy_name" className="form-control form-control-user mb-2  " placeholder="Eczane Adı" required="" id="id_pharmacy_name" />
                     
    
                    </div>

                <div className="col-md-12 mt-2">
                    <label htmlFor="id_address" className="text-md">
                        Adres
                        </label>
                      
                    <textarea onChange={handleAdress} value={address} name="address" cols="10" rows="7" className="form-control form-control-user mb-2 " placeholder="Adres" maxLength="300" id="id_address"></textarea>
                     
    
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
