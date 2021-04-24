// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

var broker = 'wss://test.mosquitto.org:8081/mqtt'; //connection address
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
})
//switch 0
var pub_switch_0 = document.getElementById('switch0');
pub_switch_0.onclick = () => {
    console.log(pub_switch_0.checked)
    client.publish('switch/switch0', String(pub_switch_0.checked))
}
//switch1
var pub_switch_1 = document.getElementById('switch1');
pub_switch_1.onclick = () => {
    console.log(pub_switch_1.checked)
    client.publish('switch/switch1', String(pub_switch_1.checked))
}
//switch
var pub_switch_2 = document.getElementById('switch2');
pub_switch_2.onclick = () => {
    console.log(pub_switch_2.checked)
    client.publish('switch/switch2', String(pub_switch_2.checked))
}


