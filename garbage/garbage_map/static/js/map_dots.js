function init()
{ 
    myMap = new ymaps.Map("map", {
        center: [52.287054, 104.281047],
        zoom: 13,
        controls: ['zoomControl']
    });
    show_dots(-1, true);
    view_index();
}

function view_index() // Отображаем все категории мусора
{
    $('#view_index').show();
    $('#view_category').hide();
    $('#view_firm').hide();
  
    show_dots(-1, true);
}
function view_category(cat_id) //Отображаем весь список точек приема мусора в сайдбаре
{ 
    $('#view_index').hide();
    $('#view_firm').hide();
    $('#view_category').show();
    cat_id == -1 ? cat_id = last_cat : last_cat = cat_id;
    $('#view_category .firmlist__item').remove();
    


    $('.recycle__subheader-category').empty();
    $('.recycle__subheader-category').append(   
        '<div class="recycle__back j-back" onclick="view_index()"></div>' +
        '<div class="recycle__subheader-category__title">' + get_category([cat_id]) + '</div>'
    ); 


    show_dots(cat_id, false);
    set_center(52.287054, 104.281047, 13);
    var firms_list = $.grep(dots, function(n, i){
        return n.categories.includes(cat_id);
    });
    for (var i = 0; i < firms_list.length; i++)
    {
        $('.firmlist').append( 
            '<div class="firmlist__item" onClick="view_firm(' + firms_list[i].id + ')"> </div>'
        );
        $('.firmlist__item:last').append(   
            '<div class="firmlist__title">' + firms_list[i].name + '</div>' +
            '<div class="firmlist__hours">' + firms_list[i].working_hours + '</div>' + 
            '<div class="firmlist__address">' + firms_list[i].addres + '</div>'
        );
    } 
}


function view_firm(firm_id) //Информация о выбранной точке
{
    $('.firmcard').remove();
    $('#view_index').hide();
    $('#view_category').hide();
    $('#view_firm').show(); 
    
    var chs_firm = $.grep(dots, function(n, i){
        return n.id === firm_id;
    });
    set_center(chs_firm[0].x, chs_firm[0].y, 16);
    $('.recycle__socfooter').before( '<div class="firmcard""> </div>');
    $('.firmcard').append(
        '<div class="firmcard__head"> ' + 
            '<div class="firmcard__title">' + chs_firm[0].name + '</div>' +
            '<div class="firmcard__address">' + chs_firm[0].addres + '</div>' + 
        '</div>'
    );
    $('.firmcard').append(
        '<div class="firmcard__photo">' +
           
        '</div>'
    );
    $('.firmcard').append(
        '<div class="firmcard__body">' +
            '<div class="firmcard__hours">' + chs_firm[0].working_hours + '</div>' +
            '<div class="firmcard__phone">+7 950 089-15-17</div>' +
            '<div class="firmcard__desc">' + chs_firm[0].description + '</div>' +
        '</div>'
    );
    $('.firmcard').append(
        '<div class="firmcard__also also">' + 
            '<span class="also__label">Также принимается</span>' + 
            '<ul class="also__list"> </ul>' +
        '</div>'
    );
   
    $('.recycle__subheader-category').empty();
    $('.recycle__subheader-category').append('<div class="recycle__back j-back" onclick="view_category(last_cat)"></div>' +
                                            '<div class="recycle__subheader-category__title"></div>'
                                            );
 

    for (var i = 0; i < chs_firm[0].categories.length; i++)
    {
        $('.also__list').append('<li>' + get_category([chs_firm[0].categories[i]]) + '</li>');
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
