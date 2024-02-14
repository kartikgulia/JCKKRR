document.getElementById('image-container').addEventListener('click', function (event) {
    var clickX = event.pageX - this.offsetLeft;
    var clickY = event.pageY - this.offsetTop;
    console.log('Distance from click point to reference point:', Math.sqrt((clickX - 0)**2 + (clickY - 0)**2));
    document.getElementById('click-point').style.left = clickX + 'px';
    document.getElementById('click-point').style.top = clickY + 'px';
});