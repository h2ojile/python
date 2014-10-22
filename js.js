function prepareMap(address, city) {
    var map = new BMap.Map("allmap");

    map.enableScrollWheelZoom();
    map.addControl(new BMap.NavigationControl()); //添加默认缩放平移控件

    var sMyGeo = new BMap.Geocoder();
    sMyGeo.getPoint(address, function(sPoint) {
        if (sPoint) {
            map.addOverlay(new BMap.Marker(sPoint));
            map.centerAndZoom(sPoint, 13);
        }
    }, city);
    return map;
}



function addMarker(item) {
    var sMyGeo = new BMap.Geocoder();
    sMyGeo.getPoint(item['address'], function(sPoint) {
        if (sPoint) {
            var marker = new BMap.Marker(sPoint);
            marker['jobitem']=item;
            map.addOverlay(marker);
            var content = "<p>"+item['description']+"</p>";
            var opts = {
                  title : "<span>"+item['salary']+"</span><a target='_blank' title='"+item['title']+"' href='"+item['url']+"'>"+item['title']+"</a>" , // 信息窗口标题
                enableMessage:true 
               };

            var infoWindow = new BMap.InfoWindow(content,opts);
            marker.addEventListener('click',
                function() {
                    this.openInfoWindow(infoWindow);
                }
            );
             marker.addEventListener('mouseover',
                function() {
                    var label = new BMap.Label(this.jobitem['title'],{offset:new BMap.Size(20,-10)});
                    this.setLabel(label)
                }
            );
             marker.addEventListener('mouseout',
                function() {
                     this.getLabel().setContent('');
                }
            );

        }
    });
}





var map = prepareMap("五角场", "上海");
var xml = new XMLHttpRequest();
xml.open('get', 'items.json', false);
xml.onreadystatechange = function() {
    if (xml.readyState == 4 && xml.status == 200) {
        var items = JSON.parse(xml.responseText);
        addPoints(items);
    }
}
xml.send();


function addPoints(items) {
    for (var i in items) {
       // if (i > 6) break;
        var item = items[i];
        addMarker(item);
    }
}
