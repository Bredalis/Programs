
const code = `
start=>start: start
output1=>output: print("\\nMultiplication Table")
output2=>output: print(f"\\n{'Table'} {number}")
condition3=>condition: for i in range(0, 11)|past
output4=>output: print(f"{i} X {number} = {i * number}")
condition5=>condition: for i in range(0, 11)|past
subroutine6=>subroutine: multiplication_tables(i)
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

const chart = flowchart.parse(code);
chart.drawSVG("canvas", {"line-width": 2});
console.log(code);

const codePre = code.replaceAll("&", "&amp;").replaceAll("<", "&lt;");
document.getElementById("code").textContent = codePre;

// Double click to copy SVG to clipboard
document.ondblclick = async () => {
    const svg = document.getElementsByTagName("svg")[0];
    if (svg) {
        await navigator.clipboard.writeText(svg.outerHTML);
        console.log("SVG copied to clipboard");
    }
};
