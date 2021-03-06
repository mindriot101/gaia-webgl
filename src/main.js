var THREE = require('three');
var $ = require('jquery');
var OrbitControls = require('three-orbit-controls')(THREE);
var Stats = require('stats.js');

var camera, scene, renderer, controls;
var canvas = document.getElementById("plotcanvas");

var WIDTH = canvas.clientWidth,
    HEIGHT = canvas.clientHeight;

var stats = new Stats();

init();
animate();


function init() {
    stats.showPanel(0);
    document.body.appendChild(stats.dom);
    scene = new THREE.Scene();

    renderer = new THREE.WebGLRenderer({
        antialias: false,
        canvas: document.getElementById("plotcanvas"),
    });
    renderer.setSize(WIDTH, HEIGHT);

    buildCamera();
    scene.add(camera);

    for (var i=0; i<16; i++) {
        (function(i) {
            $.getJSON("/data/" + i, function(data) {
                console.log("Fetched dataset " + i);
                var geometry = new THREE.Geometry();
                for (var j=0; j<data.x.length; j++) {
                    geometry.vertices.push(
                        new THREE.Vector3(data.x[j], data.y[j], data.z[j])
                    );
                }
                var material = new THREE.MeshBasicMaterial({
                    color: 0xffffff,
                });
                var points = new THREE.Points(geometry, material);
                scene.add(points);
            })
        })(i);
    }

    renderer.setClearColor(0x0a0a0a);

    var light = new THREE.PointLight(0xffffff);
    light.position.set(-100, 200, 100);
    scene.add(light);

    controls = new OrbitControls(camera);
}

function animate() {
    stats.begin();
    renderer.render(scene, camera);
    controls.update();
    stats.end();
    requestAnimationFrame(animate);
}

function buildCamera() {
    camera = new THREE.PerspectiveCamera(
        45, WIDTH / HEIGHT, 0.1, 1000
    );
    camera.position.set(0, 0, 6);
}
