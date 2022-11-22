"use strict";

const e = React.createElement;

const ItemDeleteButton = () => {
  const [change, setChange] = React.useState(null);

  const [item_list, setItemList] = React.useState([]);

  React.useEffect(() => {
    getItemList();
  }, [change]);


  const getItemList = () => {
    var csrftoken = getCookie("csrftoken");
    fetch("http://localhost:8000/getItemList", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((resp) => resp.json())
      .then((response) => setItemList(response))

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

  const DeleteItem = (id) => {
    var csrftoken = getCookie("csrftoken");
 

    fetch(`http://localhost:8000/delete/item/react/${id}`, {
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
                    <th data-priority="2">Malzeme Adı</th>
                    <th data-priority="3">Adet</th>                    
                    <th data-priority="4">Tarih</th>  
                    <th data-priority="5">Durum</th>  
                    <th data-priority="6">Sil</th>  
                  </tr>
                </thead>
                <tbody>
                  {item_list.map((order, key) => {
                    return (
                      <tr key={key}>
                        <td className="d-none"  ></td>
                        <td >
                        <a href={"/edit/item/"+ order.id}>
                          <i className="fa fa-pen-to-square fa-1x text-primary text-btn-size"></i>
                        </a>
                          
                        </td>
                        <td>
                      
                          {(order.item_name)}
                        </td>
                        <td>{parseFloat(`${order.quantity}`)}</td>
                        <td>{order.created_at}</td>
                        <td>
                          {order.status ? (
                            <i className="fa fa-check bg-success text-white p-1"></i>
                          ) : (
                            <i className="fa fa-xmark bg-danger text-white p-1 px-2"></i>
                          )}
                        </td>
                        <td>
                        <form
                      method="post"
                      action=""
                      onSubmit={(e) => {
                        e.preventDefault();
                        DeleteItem(order.id);
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
                  
                    <th>Malzeme Adı</th>
                    <th>Adet</th>   
                    <th>Tarih</th> 
                    <th ></th>               
                    <th ></th>               

                  </tr>
                </tfoot>
            </table>
    </div>
  );
};

const domContainer = document.querySelector("#item_list_container");
ReactDOM.render(<ItemDeleteButton />, domContainer);
