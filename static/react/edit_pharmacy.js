'use strict';

const e = React.createElement;

const EditPharmacyButton=()=> {

  const [screenStates, setScreenStates] = React.useState({
 
    pharmacy:  window.pharmacy,
    pharmacy_profile:  window.pharmacy_profile,
    username: window.pharmacy.username,
    address: window.pharmacy_profile.address,
    pharmacy_name: window.pharmacy_profile.pharmacy_name,
    email: window.pharmacy.email,
    pharmacy_id: window.pharmacy.pharmacy_id,
    pharmacy_profile_id: window.pharmacy_profile.pharmacy_profile_id,

  })



  console.log(screenStates.pharmacy)
  console.log(screenStates.pharmacy_profile)

  const handleInputs = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.value})

  }

  const handleCheckbox = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.checked})

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
  const EditPharmacy =() =>{
    var csrftoken = getCookie('csrftoken')
      if (screenStates.username == '' || screenStates.pharmacy_name == '' || screenStates.email == '' || screenStates.pharmacy_id == ''  || screenStates.pharmacy_profile_id == ''  ) {
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
   
        fetch(`http://localhost:8000/edit/pharmacy/${screenStates.pharmacy_id}/react`, {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"item_name":screenStates.item_name,
            "username":screenStates.username,
            "address":screenStates.address,
            "pharmacy_name":screenStates.pharmacy_name,
            "email":screenStates.email,
            "pharmacy_id":screenStates.pharmacy_id,
            "pharmacy_profile_id":screenStates.pharmacy_profile_id})
    
        }).then(resp => resp.json())
        .then(resp =>             
          (iziToast.show({message:"Eczane başarılı bir şekilde güncellendi.", position: "topRight",
          messageColor: 'black',
          messageSize: '16',
          title: 'Başarılı',
          titleColor: 'black',
          titleSize: '16',
          maxWidth: '600',
          backgroundColor: '#89D99D',
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
                  <i className="fa fa-plus">  </i>    Eczane Düzenle
                  </h6>  
              </div>
              <form method="post" action="" onSubmit={(e)=>{
                e.preventDefault()
                
                EditPharmacy()
              }}>
                
                <div className="row ">
            <div className="col-md-12 mt-2">
                <label htmlFor="id_username" className="text-md">
                    Username
                    </label>
                      
                    <input value={screenStates.username} onChange={handleInputs} type="text" name="username" className="form-control form-control-user" placeholder="Username" maxLength="150" autoFocus="" required="" id="id_username" />
                     
           
            </div>
            <div className="col-md-12 mt-2">
                <label htmlFor="id_email" className="text-md">
                    Email
                    </label>
                  
                <input value={screenStates.email} onChange={handleInputs} type="email" name="email" className="form-control form-control-user" placeholder="Email" max="40" required="" id="id_email" />
                 
            </div>



                <div className="col-md-12 mt-2">
                    <label htmlFor="id_pharmacy_name" className="text-md">
                        Eczane Adı
                        </label>
                      
                    <input value={screenStates.pharmacy_name} onChange={handleInputs} type="text" name="pharmacy_name" className="form-control form-control-user mb-2  " placeholder="Eczane Adı" required="" id="id_pharmacy_name" />
                     
    
                    </div>

                <div className="col-md-12 mt-2">
                    <label htmlFor="id_address" className="text-md">
                        Adres
                        </label>
                      
                    <textarea value={screenStates.address} onChange={handleInputs} name="address" cols="10" rows="7" className="form-control form-control-user mb-2 " placeholder="Adres" maxLength="300" id="id_address"></textarea>
                     
    
                    </div>
        </div>



                      <button 
                    type="submit"
                    className="px-5 py-2 mr-3 mt-3 font-bold text-center text-white uppercase btn bg-primary"
                    id="submit_button"
                    >
                    <i className="fa fa-plus">  </i> Düzenle
                    </button>
                  
              </form>
        </div>




        

        
      </div>

    );
 
}

const domContainer = document.querySelector('#edit_pharmacy_container');
ReactDOM.render(<EditPharmacyButton />, domContainer);
