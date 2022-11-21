'use strict';

const e = React.createElement;

const OrderConfirmButton=()=> {

  const [screenStates, setScreenStates ] = React.useState({
    item_name: "",
    quantity: 0,
    status:false,
  
  })
  const handleInputs = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.value})

  }

  const handleCheckbox = (e) =>{
    setScreenStates({...screenStates,[e.target.name]:e.target.checked})
    
  }



  const [order_list, setUserList] =  React.useState([])
  React.useEffect(() => {
    getOrderList();
  

 
},[])


console.log(order_list)



const getUsername =(id,key) =>{
  var csrftoken = getCookie('csrftoken')
  fetch(`http://localhost:8000/getUsername/${id}`, {
    'method':'GET',
    headers: {
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,  
      }, 
     

  }).then(resp => resp.json())

   .then(resp => document.getElementsByClassName("getusername")[`${key}`].innerHTML=resp)
   
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
const getItemname =(id,key) =>{
  var response=""
  var csrftoken = getCookie('csrftoken')
  fetch(`http://localhost:8000/getItemname/${id}`, {
    'method':'GET',
    headers: {
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,  
      }, 
     

  }).then(resp => resp.json())
    .then(resp => document.getElementsByClassName("getitemname")[`${key}`].innerHTML=resp)

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
  console.log(response)
  return response

}

  const getOrderList =() =>{
    var csrftoken = getCookie('csrftoken')
    fetch('http://localhost:8000/getOrderList', {
      'method':'GET',
      headers: {
          'Content-Type':'application/json',
          'X-CSRFToken':csrftoken,  
        }, 
       
  
    }).then(resp => resp.json())
     .then(response => setUserList(response))
      
     
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


  const ConfirmOrder =(id) =>{
    var csrftoken = getCookie('csrftoken')
    console.log(id)

        fetch(`http://localhost:8000/confirm/order/react/${id}`, {
          'method':'POST',
          headers: {
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,  
            }, 
            body:JSON.stringify({"id":id})
    
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


 
    return (
      <div>


                    <table  id="example"  className="table table-striped nowrap w-100" >
                        <thead>
                            <tr>
                              <th data-priority="0" className="d-none">Id</th>
                             
                              <th data-priority="1">Eczane</th>
                              <th data-priority="2">Malzeme Adı</th>
                              <th data-priority="3">Adet</th>                    
                              <th data-priority="4">Tarih</th>                    
                              <th data-priority="5">Durum</th>                    
                            </tr>               
                          </thead>
                          <tbody>
                          {order_list.map((order,key)=>{
                              return(
                                <tr>
                                 
                                <td className="d-none"></td>
                                <td className="getusername">{getUsername(order.user_id,key)}</td>
                                <td className="getitemname">{getItemname(order.item_name_id,key)}</td>
                                <td>
                                {order.quantity}
                                </td>
                                <td>
                                {order.created_at}
                                </td>
                                <td>
                          
                                  {order.status ?                                   
                                        <button className="btn bg-success btn-sm text-white text-sm  p-1 px-2">
                                          <i className="fa fa-check" ></i> 
                                          <span className="text-sm text-capitalize text-white ">Onaylandı</span>
                                        </button>
                                        :<form method="post" action="" onSubmit={(e)=>{
                                          e.preventDefault()
                                          ConfirmOrder(order.id)
                                        }}><button className="btn btn-danger btn-sm text-white text-sm">
                                          <i className="fa fa-clock" > </i> 
                                          <span className=" text-sm text-capitalize text-white "> Onayla</span>
                                        </button>
                                        </form> 
                                      }
          
                                </td>
                                            
                              </tr>
                               
                              

                                );

                            })}

  
                          </tbody>
                            <tfoot>
                              <tr >
                                <th className="d-none">Id</th>
                         
                                <th>Eczane</th>  
                                <th>Malzeme Adı</th>
                                <th>Adet</th>   
                                <th>Tarih</th>                      
                                <th></th>               
                              </tr>
                            </tfoot>
                      </table>
 
      </div>

    );
 
}

const domContainer = document.querySelector('#order_confirm_container');
ReactDOM.render(<OrderConfirmButton />, domContainer);
