'use strict';

const e = React.createElement;




// import React, {useState, useEffect} from 'react'
const OrderItemButton=()=> {

  const [screenStates, setScreenStates] = React.useState({
    item_name: "",
    quantity: 0,
    user:window.user,
    item_list:[],
    
  })

  React.useEffect(() => {
  
    getItemList();
    getToken();
},[])



  const handleInputs = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.value})

  }

  const getToken = ()  => {
    var csrftoken = getCookie('csrftoken')
    let input_token=document.getElementsByName("csrfmiddlewaretoken")[0]

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


  const OrderItem =(e) =>{
 
      var csrftoken = getCookie('csrftoken')
      if (screenStates.item_name == '' || screenStates.quantity == ''  || e.target.firstChild.firstChild.firstChild.nextElementSibling.value == '' ) {
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
        fetch('http://localhost:8000/order/item/react', {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"item_name":screenStates.item_name,"quantity":screenStates.quantity,"user":screenStates.user})
    
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
          .then(e.target.reset())
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


  const getItemList =() =>{

      fetch('http://localhost:8000/getItemList', {
        'method':'GET',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':screenStates.csrftoken,  
          }, 
         

      }).then(resp => resp.json())
        .then(response => setScreenStates({...screenStates,item_list:response}))
        

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

    return (
      <div>

        <div className="card w-50 mx-auto p-4">
              <div className="card-header py-3 mb-3">
                  <h6 className="m-0 font-weight-bold text-primary">  
                  <i className="fa fa-plus">  </i>    Sipariş Oluştur
                  </h6>  
              </div>
              <form method="post" action="" onSubmit={(e)=>{
                e.preventDefault()
                
                OrderItem(e)
              }}>
                
                  <div className="row ">
                      

                      <div className="col-md-12">
                          <label htmlFor="id_item_name" className="text-md">
                              Malzeme Adı
                              </label>              
                    
                            <select onChange={handleInputs} name="item_name" className="form-control form-control-user " placeholder="Malzeme" type="text" required="" id="id_item_name">

                              <option value="" >---------</option>
                           
                              {screenStates.item_list.map((item,key)=>{
                              return(
                                <option value={item.id} > {item.item_name} </option>
                              

                                );

                            })}

                              
                            </select>  
                    
                        </div>

                      <div className="col-md-12 mt-2">
                      <label htmlFor="id_quantity" className="text-md">
                          Adet
                      </label>
                    
                      <input type="number"  name="quantity" onChange={handleInputs} className="form-control form-control-user " placeholder="Adet" required="" id="id_quantity"/>   
                      
                      </div>

  


                  </div>
                      <button 
                    type="submit"
                    className="px-5 py-2 mr-3 mt-3 font-bold text-center text-white uppercase btn bg-primary"
                    id="submit_button"
                    >
                    <i className="fa fa-plus">  </i> Siperiş Ver
                    </button>
                  
              </form>
        </div>




        

        
      </div>


    );
 
}

const domContainer = document.querySelector('#order_item_container');
ReactDOM.render(<OrderItemButton />, domContainer);
