

function init()
{ 
    myMap = new ymaps.Map("map", {
        center: [52.287054, 104.281047],
        zoom: 13,
        controls: ['zoomControl']
    });
    show_dots(-1, true);
}

function view_index() // Отображаем все категории мусора
{
    $('#view_index').show();
    $('#view_category').hide();
    $('#view_firm').hide();
    show_dots(-1, true);
  //  f(true, false, false);
}
/*
function f(a, b, c)
{
    a ? $('#view_index').show() : $('#view_index').hide();
    b ? $('#view_category').show(): $('#view_category').hide();
    c ? $('#view_firm').show() : $('#view_firm').hide();
}
*/
function view_category(cat_id) //Отображаем весь список точек приема мусора в сайдбаре
{
    cat_id == -1 ? cat_id = last_cat: last_cat = cat_id;
    $('div#view_category .firm').remove();
    $('#view_index').hide();
    $('#view_category').show();
    $('#view_firm').hide();
    $('h2#title_garbage').text(get_category([cat_id]));
    show_dots(cat_id, false);
    set_center(52.287054, 104.281047, 13)
    var firms_list = $.grep(dots, function(n, i){
        return n.categories.includes(cat_id);
    });
    for (var i = 0; i < firms_list.length; i++)
    {
        $('#view_category').append( '<div class = "firm" onClick="view_firm(' + firms_list[i].id + ')"> </div>');
        $('.firm:last').append( '<h3>' + firms_list[i].name + '</h3>' +
                                '<p id="hours">' + firms_list[i].working_hours + '</p>' + 
                                '<p id="addres">' + firms_list[i].addres + '</p>'
        );
    }
}


function view_firm(firm_id) //Информация о выбранной точке
{
    $('div#view_firm #about_firm').remove();
    $('#view_index').hide();
    $('#view_category').hide();
    $('#view_firm').show(); 
    var chs_firm = $.grep(dots, function(n, i){
        return n.id === firm_id;
    });
    set_center(chs_firm[0].x, chs_firm[0].y, 16);
    $('#view_firm').append( '<div id="about_firm""> </div>');
    $('#about_firm').append(    '<div class="firm_title"> ' + 
                                    '<h3>' + chs_firm[0].name + '</h3>' +
                                    '<p>' + chs_firm[0].addres + '</p>' + 
                                '</div>');

    $('#about_firm').append(    '<img src="' + chs_firm[0].image + '"/>' +
                                '<p class="inform">' + chs_firm[0].working_hours + '</p>' + 
                                '<p class="inform">' + chs_firm[0].description + '</p>' + 
                                '<p class="inform_2"> Также принимается </p>' +
                                '<div id="another_cat"> </div>'
    );
    for (var i = 0; i < chs_firm[0].categories.length; i++)
    {
        $('#another_cat').append('<div class="bloc_cat"><p>' + get_category([chs_firm[0].categories[i]]) + '</p></div>');
    }

}

function show_dots(category_filter, check)
{
    myMap.geoObjects.removeAll();
    for (var i = 0; i < dots.length; i++)
    {
        if (check || dots[i].categories.includes(category_filter))
        { 
            myMap.geoObjects           
                .add(new ymaps.Placemark([dots[i].x, dots[i].y], {
                    balloonContentHeader: 
                        '<a href = "#">' + dots[i].name + '</a><br>' +
                        '<span class="description">' + dots[i].description + '</span>' + 
                        '<p>Здесь принимают ' + get_category(dots[i].categories) + ' </p>',
                    balloonContentBody: 
                        '<img src="' + dots[i].image + '" height="150" width="200"> <br/> ' +
                        '<p>' + dots[i].working_hours + '</p>',
                    hintContent: 
                        dots[i].name
                })); 
        }
    }
}
function get_category(garbage_categories)
{
    var names_of_categories = []
    for (var j = 0; j < categories.length; j++)
    {
        if (garbage_categories.includes(categories[j].id))
        {
            names_of_categories.push(categories[j].name);
        }
    }
    return names_of_categories.join(", ");
}

function set_center(x, y, zoom)
{
    myMap.setCenter([x, y], zoom, {
        checkZoomRange: true
    });
}
