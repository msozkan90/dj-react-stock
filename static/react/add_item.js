'use strict';

const e = React.createElement;

const AddItemButton=()=> {


  const [item_name, setItemName] = React.useState("");
  const [quantity, setQuantity] = React.useState(0);
  const [status, setStatus] = React.useState(false);
  const handleItemInputs = (e) =>{

    setItemName(e.target.value)
  }
  const handleQuantityInputs = (e) =>{
    setQuantity(e.target.value)
   

  }

  const handleCheckbox = (e) =>{

    setStatus(e.target.checked)
    

  }

  const clearState = () =>{
    setStatus(false)
    setQuantity(0)
    setItemName("")
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

  const AddItem =() =>{
    console.log(item_name)
    console.log(quantity)
    console.log(status)
    var csrftoken = getCookie('csrftoken')
      if (item_name == '' || quantity == ''   ) {
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
        fetch('http://localhost:8000/add/item/react', {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"item_name":item_name,"quantity":quantity,"status":status})
    
        }).then(resp => resp.json())
        .then(resp =>             
          (iziToast.show({message:"Malzeme başarılı bir şekilde eklendi", position: "topRight",
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
          transitionOut: 'flipOutX',})
          ))
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
          console.log('ERROR:', error)
        })
    
      }

  }


 
    return (
      <div>

        <div className="card w-50 mx-auto p-4">
              <div className="card-header py-3 mb-3">
                  <h6 className="m-0 font-weight-bold text-primary">  
                  <i className="fa fa-plus">  </i>    Malzeme Ekle
                  </h6>  
              </div>
              <form method="post" action="" onSubmit={(e)=>{
                e.preventDefault()
                AddItem()
              }}>
                  <input type="hidden" name="csrfmiddlewaretoken" value="Skp7lm9HhnLMOJos2eXpgOXiT8BhhApnmwgNRYbKKX4dXNhuIkdSO9YZ5a0W96J9"/>

                  <div className="row ">
                      
                      <div className="col-md-12">
                          <label htmlFor="id_item_name" className="text-md">
                          Malzeme Adı
                          </label>               
                          
                      <input type="text" name="item_name" onChange={handleItemInputs} value={item_name} className="form-control form-control-user " placeholder="Malzeme Adı" maxLength="60" required="" id="id_item_name" />  
                              
                      </div>
                      <div className="col-md-12 mt-2">
                      <label htmlFor="id_quantity" className="text-md">
                          Adet
                      </label>
                    
                      <input type="number"  name="quantity" onChange={handleQuantityInputs} value={quantity} className="form-control form-control-user " placeholder="Adet" required="" id="id_quantity"/>   
                      
                      </div>
                      <div className="col-md-12 mt-2">
                          <label htmlFor="id_status" className="text-md">
                              Durum
                          </label>
                       
                          <input onChange={handleCheckbox} type="checkbox" name="status" className="form-control-user mt-3 ml-2 " placeholder="Durum" id="id_status" checked={status}/>   
                          
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

const domContainer = document.querySelector('#add_item_container');
ReactDOM.render(<AddItemButton />, domContainer);
