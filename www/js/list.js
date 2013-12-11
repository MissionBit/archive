var clearList = function(list) {
    list.innerHTML = '';
};

var populateList = function(list, members) {
        
    for(i=0; i < members.length; i++) {
        var li = document.createElement("li");

        var img = document.createElement("img");
        img.setAttribute("src", "http://lorempixum.com/40/40/nature/1");

        var h3 = document.createElement("h3");
        h3.innerHTML = members[i];

        var p = document.createElement("p");
        p.innerHTML = "Hi";

        li.appendChild(img);
        li.appendChild(h3);
        li.appendChild(p);
        
        list.appendChild(li);
    }
};

var refreshList = function(list, members) {
    clearList(list);
    populateList(list, members);
};
