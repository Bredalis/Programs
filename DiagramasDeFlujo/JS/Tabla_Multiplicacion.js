
code = `
start=>start: start
output1=>output: print("\nTabla de Multiplicacion")
output2=>output: print(f"\n{"Tabla"} {numero}")
condition3=>condition: for i in range(0, 11)|past
output4=>output: print(f"{i} X {numero} = {i * numero}")
condition5=>condition: for i in range(0, 11)|past
subroutine6=>subroutine: tablas_muplicacion(i)
end=>end: end
start->output1
output1->output2
output2->condition3
condition3(yes)->output4
output4(left)->condition3
condition3(no)->condition5
condition5(yes)->subroutine6
subroutine6(left)->condition5
condition5(no)->end
`;

chart = flowchart.parse(code);
chart.drawSVG("canvas", {"line-width": 2});
console.log(code);

var code_pre = code.replaceAll("&", "&amp;").replaceAll("<", "&lt;");
document.getElementById("code").innerHTML = code_pre;

// double click to copy svg to clipboard
document.ondblclick = async () => {
	var svg = document.getElementsByTagName("svg")[0];
	await navigator.clipboard.writeText(svg.outerHTML);
}