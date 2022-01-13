$('document').ready(function(){
    let arr = Array.from({length : 40}, (_, v) => v + 1)

    const shuffleArray = arr => {
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
        }
    }

    shuffleArray(arr);

    arr.slice(0,32).forEach(function(val,idx){
        var id = "#q" + val.toString();
        $(id).remove(); 
    });
})
