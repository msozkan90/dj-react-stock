"use strict";

const e = React.createElement;

const PharmacyDeleteButton = () => {
  const [change, setChange] = React.useState(null);

  const [user_list, setUserList] = React.useState([]);

  React.useEffect(() => {
    getPharmacyList();
  }, [change]);


  const getPharmacyList = () => {
    var csrftoken = getCookie("csrftoken");
    fetch("http://localhost:8000/getUserList", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((resp) => resp.json())
      .then((response) => setUserList(response))

      .catch(function (error) {
        iziToast.show({
          message: "Lütfen formu doğru bir şekilde doldurun",
          position: "topRight",
          messageColor: "black",
          messageSize: "16",
          title: "Başarısız",
          titleColor: "black",
          titleSize: "16",
          maxWidth: "600",
          backgroundColor: "#f34444",
          iconColor: "#fff",
          progressBarColor: "black",
          resetOnHover: true,
          transitionIn: "flipInX",
          transitionOut: "flipOutX",
        });
        console.log("ERROR:", error);
      });
  };
  const getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };
  const getUsername = (id, key) => {
    var csrftoken = getCookie("csrftoken");
    fetch(`http://localhost:8000/getUserprofile/${id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((resp) => resp.json())

      .then(
        (resp) =>
          (document.getElementsByClassName("getusername")[`${key}`].innerHTML =
            resp)
      )

      .catch(function (error) {

        console.log("ERROR:", error);
      });
  };
  const DeletePharmacy = (id) => {
    var csrftoken = getCookie("csrftoken");
 

    fetch(`http://localhost:8000/delete/pharmacy/react/${id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ id: id }),
    })
      .then((resp) => resp.json())
      .then((resp) =>
        iziToast.show({
          message: resp["message"],
          position: "topRight",
          messageColor: "black",
          messageSize: "16",
          title: resp["type"],
          titleColor: "black",
          titleSize: "16",
          maxWidth: "600",
          backgroundColor: resp["color"],
          iconColor: "#fff",
          progressBarColor: "black",
          resetOnHover: true,
          transitionIn: "flipInX",
          transitionOut: "flipOutX",
        })
      )
      .then((resp) => setChange(Math.random().toString(36).substring(2, 7)))

      .catch(function (error) {
        iziToast.show({
          message: "Lütfen formu doğru bir şekilde doldurun",
          position: "topRight",
          messageColor: "black",
          messageSize: "16",
          title: "Başarısız",
          titleColor: "black",
          titleSize: "16",
          maxWidth: "600",
          backgroundColor: "#f34444",
          iconColor: "#fff",
          progressBarColor: "black",
          resetOnHover: true,
          transitionIn: "flipInX",
          transitionOut: "flipOutX",
        });
        console.log("ERROR:", error);
      });
  };


  return (
    <div>
    
           <table id="example" className="table table-striped nowrap w-100">
                <thead>
                  <tr>
                  <th data-priority="0" className="d-none">Id</th>
                  <th data-priority="1">Düzenle</th>
                  <th data-priority="2">Kullanıcı Adı</th>
                  <th data-priority="3">Eczane Adı</th>                     
              
                    <th data-priority="5">Sil</th>  
                  </tr>
                </thead>
                <tbody>
                  {user_list.map((order, key) => {
                    return (
                      <tr key={key}>
                        <td className="d-none"  >{order.id}</td>
                         <td >
                        <a href={"/edit/pharmacy/"+ order.id}>
                          <i className="fa fa-pen-to-square fa-1x text-primary text-btn-size"></i>
                        </a>
                          
                        </td>
                        <td>    
                      
                          {(order.username)}
                        </td>
                        <td className="getusername">{getUsername(order.id, key)}</td>
                  
         
                        <td>
                        <form
                      method="post"
                      action=""
                      onSubmit={(e) => {
                        e.preventDefault();
                        DeletePharmacy(order.id);
                      }}
                    >
                        <button className="btn bg-dark btn-sm text-white text-sm  p-1 px-2">
                      <i className="fa fa-trash"> </i>                  
                      </button>
                      </form>    
                        </td>
                      </tr>
                    );
                  })}       
                </tbody>
                <tfoot>
                  <tr>
                
                  <th className="d-none">Id</th>
                  <th ></th>
                  <th>Kullanıcı Adı</th>                                
                  <th>Eczane Adı</th>               
                  <th ></th>
                      
                                                              

                  </tr>
                </tfoot>
            </table>
   
    </div>
  );
};

const domContainer = document.querySelector("#pharmacy_list_container");
ReactDOM.render(<PharmacyDeleteButton />, domContainer);
