function post_likes(post_id,model_id,pid){
		$.ajax({
			url:"/api/model/add/posts/likes",
			method:'POST',
			data:{post_id,model_id,pid},
			success:function(response){
				alert(response.message);
			}
		});
	}

fileImageUloader();
	$(document).ready(function(){
		$(".cft").on('click',function(){
			 var filetype= $(this).data('value');
			 if(filetype=='video'){
			 	fileVideoUploader();
			 }else{
			 	fileImageUloader();
			 }
		});
	});
	function fileImageUloader(){
			FilePond.registerPlugin(
			FilePondPluginImagePreview,
			FilePondPluginImageCrop,
			FilePondPluginImageEdit,
			FilePondPluginImageTransform,
			FilePondPluginFileValidateType
		);

			 

        const inputElement = document.querySelector("#fileUpload");
        const post_img_arr=[];
        var path ='';
        const pond = FilePond.create(inputElement, {

        	allowFileTypeValidation:true,
			acceptedFileTypes:['image/jpg','image/jpeg','image/png'],
        	allowImageCrop:true,
        	imageCropAspectRatio:'4:5',
            allowMultiple: true,
            allowImagePreview:true,
            allowReorder: true,
            allowReplace: true,
            name: 'post_media_img',
            instantUpload: true,
            onaddfile: () => {
                console.log('add');
            },
            onremovefile: () => {
                console.log('remove');
            },
            server: {
                  process: {
                        url: "/api/model/upload/post/image",
                        method: 'POST',
                        withCredentials: false,
                        headers: {},
                        onload: (response) => {
							response = JSON.parse(response);
                        	path = response.filepath;
                        	post_img_arr.push(path);
                        	var ele='<input type="hidden" name="post_media_img_path" value="'+post_img_arr.toString()+'"/>';
                        	$("#pstu").html(ele);
                        },
                        onerror: console.log,
                        ondata: null
                  },
            }
        });
	}

	function fileVideoUploader(){
		FilePond.registerPlugin(
			FilePondPluginFileValidateType
			);
			const inputElement = document.querySelector("#fileUpload");
			const pondvideo = FilePond.create(inputElement, {
				allowFileTypeValidation:true,
				acceptedFileTypes:['video/mp4', 'video/avi', 'video/mov'],
				allowReorder: true,
				allowReplace: true,
				name: 'post_media_vid',
				instantUpload: true,
				onaddfile: () => {
					console.log('add');
				},
				onremovefile: () => {
					console.log('remove');
				},
				server: {
					  process: {
							url: "/api/model/upload/post/video",
							method: 'POST',
							withCredentials: false,
							headers: {},
							onload: (response) => {
								response = JSON.parse(response);
                        		var path = response.filepath;
                        		var ele = '<input type="hidden" name="post_media_vid_path" value="'+path+'"/>';
                        		$("#pstu").html(ele);
                        	},
							onerror: console.log,
							ondata: null
					  },
				}
			});
	}


	FilePond.registerPlugin(
				FilePondPluginFileValidateType
			);
			const inputElement = document.querySelector("#clipUpload");
			const pondvideo = FilePond.create(inputElement, {
				allowFileTypeValidation:true,
				acceptedFileTypes:['video/mp4', 'video/avi', 'video/mov'],
				allowReorder: true,
				allowReplace: true,
				name: 'clip_video',
				instantUpload: true,
				onaddfile: () => {
					console.log('add');
				},
				onremovefile: () => {
					console.log('remove');
				},
				server: {
					  process: {
							url: "/api/model/upload/clip",
							method: 'POST',
							withCredentials: false,
							headers: {},
							onload: (response) => {
								response = JSON.parse(response);
                        		var path = response.filepath;
                        		var clip_trailer = response.clip_trailer;
                        		var clip_thumbs = response.clip_paths;
                        		var duration = response.duration;
                        		var ele = '<input type="hidden" name="clip_path" value="'+path+'"/>'+
                        		            '<input type="hidden" name="clip_trailer" value="'+clip_trailer+'"/>'+
                        		            '<input type="hidden" name="clip_thumbs" value="'+clip_thumbs+'"/>'+
                        		           '<input type="hidden" name="duration" value="'+duration+'"/>';
                        		$("#clipDiv").html(ele);
                        	},
							onerror: console.log,
							ondata: null
					  },
				}
			});

	FilePond.registerPlugin(
                FilePondPluginImagePreview,
                FilePondPluginImageCrop,
                FilePondPluginImageEdit,
                FilePondPluginImageTransform,
                FilePondPluginFileValidateType
            );
			const inputElementg = document.querySelector("#galleryUpload");
			const pondgallery = FilePond.create(inputElementg, {
			    allowMultiple:true,
                allowImagePreview:true,
				allowFileTypeValidation:true,
				acceptedFileTypes:['image/jpg','image/jpeg','image/png'],
				allowReorder: true,
				allowReplace: true,
				name: 'gallery_image',
				instantUpload: true,
				onaddfile: () => {
					console.log('add');
				},
				onremovefile: () => {
					console.log('remove');
				},
				server: {
					  process: {
							url: "/api/model/upload/gallery",
							method: 'POST',
							withCredentials: false,
							headers: {},
							onload: (response) => {
								response = JSON.parse(response);
                                console.log(response);
                        	},
							onerror: console.log,
							ondata: null
					  },
				}
			});


	FilePond.registerPlugin(
			FilePondPluginFileValidateType
			);
			const inputElementshow = document.querySelector("#lvshd");
			const liveshow = FilePond.create(inputElementshow, {
				allowFileTypeValidation:true,
				acceptedFileTypes:['video/mp4', 'video/avi', 'video/mov'],
				allowReorder: true,
				allowReplace: true,
				name: 'show_video',
				instantUpload: true,
				onaddfile: () => {
					console.log('add');
				},
				onremovefile: () => {
					console.log('remove');
				},
				server: {
					  process: {
							url: "/api/model/upload/live/show",
							method: 'POST',
							withCredentials: false,
							headers: {},
							onload: (response) => {
								response = JSON.parse(response);
                        		var path = response.filepath;
                        		var ele = '<input type="hidden" name="live_show_trailer" value="'+path+'"/>';
                        		$("#lvswf").html(ele);
                        	},
							onerror: console.log,
							ondata: null
					  },
				}
	});

    $(".cp_shlk").on('click', function(){
        var url = $(this).data('url');
        Clipboard_CopyTo(url)
        show_toast_message('Link copied to clipboard.')
    })
	function Clipboard_CopyTo(value) {
	  var tempInput = document.createElement("input");
	  tempInput.value = value;
	  document.body.appendChild(tempInput);
	  tempInput.select();
	  document.execCommand("copy");
	  document.body.removeChild(tempInput);
	}

    $(".rpt_is").on('click',function(){
        $("#post_repo_").modal();
        var post_id = $(this).data('post_id');
        $("#post_id").val(post_id);
    });
    $('#issue_form').on('submit',function (e) {
        $.ajax({
            url: "{{url_for('add_post_report')}}",
            method: 'POST',
            data: $('#issue_form').serialize(),
            beforeSend:function(){
            },
            success: function (response) {
               $("#post_repo_").modal('toggle');
               show_toast_message(response.message)
            }
        });
        e.preventDefault();
    });