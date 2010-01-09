// пагинатор
// передвигаем ползунок
function mv(d)
{
    //d - направление движения
    cur = parseInt($(v1).attr('innerHTML'));
    // считаем ускорение
    m = 0;
    //if (iter > 40) m = 30;
    //else if (iter > 20) m = 7;
   // else if (iter > 10) m = 2;
    //проверки в зависимости от направляения
    if (d == 1)
    {
        if (cur + 12 > maxPage) return;
        if (cur + m >= maxPage) m = 0;
    }
    else if (cur <= 1) return;
    else if ((cur - m) <= 1) m = 0;
    if (d == 1)
        $(moveBack).css('visibility', 'visible');
    else
        $(moveForw).css('visibility', 'visible');
    cur += d * (m + 1);
    // перебираем все элементы пагинатора и меняем их
    for (i = 0; i < 12; i += 1)
    {
        obj = $('#v'+(i+1)).attr('innerHTML', cur + i ).attr('href',urlB + (cur + i) +  urlA)
        if (cur + i == act)
            $(obj).addClass('act')
        else
            $(obj).removeClass('act')
        if (cur + i == 1)// тоесть у нас нарисовался первый элемент - убираем в начало
        {
            rmv()
            $(moveBack).css('visibility', 'hidden');
        }
        else if (cur + i == maxPage)
        {
            rmv()
            $(moveForw).css('visibility', 'hidden');
        }
    }
    iter += 1;
    tid = window.setTimeout('mv('+d+')', 100);
    return false;
}
// убираем счетчик
function rmv()
{
    iter = 0;
    if (tid)
        window.clearTimeout(tid);
}
function removeAllSWFFromBlock(block)
{
	$(block + ' .player object').each(function() {
		$(this).parent().html('<a href="javascript:loadSWF('+ $(this).attr('id').substr(4) +');" id="card'+ $(this).attr('id').substr(4) +'" class="cardsblock"><img src="/images/player.gif" alt="слушать" width="64" height="67"></a>');
	});

}
function checkCNum(obj)
{
	var numChars = obj.number.value.length;
	var disValue = (numChars>=8 && numChars<=13) ? false : true;
	toggleFormDisabled(disValue);
}

function toggleFormDisabled(val)
{
    $('.btn').attr('disabled', val ? 'disabled' : false);
}
function CheckNumericKeyInfo($char, $mozChar, obj) {
	if($mozChar != null) { // Look for a Mozilla-compatible browser
	    if(($mozChar >= 48 && $mozChar <= 57) || $mozChar == 0 || $char == 8 || $mozChar == 13) $RetVal = true;
	   	else {
		     $RetVal = false;
	   	}
	}
	else { // Must be an IE-compatible Browser
	     if(($char >= 48 && $char <= 57) || $char == 13) $RetVal = true;
    else {
	       $RetVal = false;
	     }
	}

	if ( ($char == 13 || $mozChar == 13 )&& !$('#btn').attr('disabled'))
		$('#sendForm').submit();

	return $RetVal;
}
