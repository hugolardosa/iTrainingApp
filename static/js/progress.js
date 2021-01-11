function progressValue(){  
	$('.progress-bar').each(function(){    
	  var positionProgressValue = $(this).children('.progress-value').css('left','auto');
	  var progressBarValue = $(this).children('.progress-value').html();    
	  $(this).width(progressBarValue);    
	  if($(this).width() < 21){
		positionProgressValue.css('left','0');
	  }    
	});
  }
  progressValue();
  $(window).resize(function(){
	progressValue();
  });
				   
  
	  
  
  
  
  