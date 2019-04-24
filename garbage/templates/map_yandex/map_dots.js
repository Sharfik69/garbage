ymaps.ready(init);    
function init(){ 
    var myMap = new ymaps.Map("map", {
        center: [52.29778, 104.29639],
        zoom: 3
    });
    myMap.geoObjects      
    {% for dot in dots %}              
        .add(new ymaps.Placemark([{{ dot.dot_x }}, {{ dot.dot_y }}], {
            balloonContent: '{{ dot.subject }}',
            iconCaption: ''
        }))
    {% endfor %}
    ;
}