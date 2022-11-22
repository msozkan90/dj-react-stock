'use strict';

const e = React.createElement;

const EditItemButton=()=> {

  const [screenStates, setScreenStates] = React.useState({
 
    item:  window.item,
    item_name: window.item.item_name,
    quantity: window.item.quantity,
    status: window.item.status,
    id: window.item.id,

  })


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
  const EditItem =() =>{
    var csrftoken = getCookie('csrftoken')
      if (screenStates.item_name == '' || screenStates.quantity == ''   ) {
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
       
        fetch(`http://localhost:8000/edit/item/${screenStates.id}/react`, {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"item_name":screenStates.item_name,"quantity":screenStates.quantity,"status":screenStates.status})
    
        }).then(resp => resp.json())
        .then(resp =>             
          (iziToast.show({message:resp["message"], position: "topRight",
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
     
        })
    
      }

  }


 
    return (
      <div>

        <div className="card w-50 mx-auto p-4">
              <div className="card-header py-3 mb-3">
                  <h6 className="m-0 font-weight-bold text-primary">  
                  <i className="fa fa-plus">  </i>    Malzeme Düzenle
                  </h6>  
              </div>
              <form method="post" action="" onSubmit={(e)=>{
                e.preventDefault()
                EditItem()
              }}>
   
                  <input type="hidden" name="csrfmiddlewaretoken" value="Skp7lm9HhnLMOJos2eXpgOXiT8BhhApnmwgNRYbKKX4dXNhuIkdSO9YZ5a0W96J9"/>

                  <div className="row ">
                      
                      <div className="col-md-12">
                          <label htmlFor="id_item_name" className="text-md">
                          Malzeme Adı
                          </label>               
                          
                      <input type="text" name="item_name" value={screenStates.item_name} onChange={handleInputs} className="form-control form-control-user " placeholder="Malzeme Adı" maxLength="60" required="" id="id_item_name" />  
                              
                      </div>
                      <div className="col-md-12 mt-2">
                      <label htmlFor="id_quantity" className="text-md">
                          Adet
                      </label>
                    
                      <input type="number" value={screenStates.quantity}  name="quantity" onChange={handleInputs} className="form-control form-control-user " placeholder="Adet" required="" id="id_quantity"/>   
                      
                      </div>
                      <div className="col-md-12 mt-2">
                          <label htmlFor="id_status" className="text-md">
                              Durum
                          </label>
                       
                          <input onChange={handleCheckbox} type="checkbox" name="status" className="form-control-user mt-3 ml-2" placeholder="Durum" id="id_status" checked={screenStates.status}/>   
                          
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

const domContainer = document.querySelector('#edit_item_container');
ReactDOM.render(<EditItemButton />, domContainer);
