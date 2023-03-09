var mList = {
	Kannur : ['Thalassery','Payyannur','Kannur-South'],
	Kozhikode :  ['Kakanchery','Maanachira'],
	Thrissur :  ['Kunnamkulam','Chavakad'],
	Ernakulam :  ['Aluva','Palarivattom','North-Paravoor'],
	Kasargod :  ['Kanhangad','Hosdurg','Balla'],


};

el_parent = document.getElementById("parent_select");
el_child = document.getElementById("child_select");

for (key in mList) {
	el_parent.innerHTML = el_parent.innerHTML + '<option>'+ key +'</option>';
}

el_parent.addEventListener('change', function populate_child(e){
	el_child.innerHTML = '';
	itm = e.target.value;
	if(itm in mList){
			for (i = 0; i < mList[itm].length; i++) {
				el_child.innerHTML = el_child.innerHTML + '<option>'+ mList[itm][i] +'</option>';
			}
	}
});
