var http = require('http');  
var url = require('url');
var exec = require('child_process').exec; 
var dlog = console.log
var createServer = http.createServer

//创建一个服务
var server = createServer(function (req, resp) {  
   	//获得路径 url/path
	resp.writeHead(200, {'Content-Type': 'text/plain'});  
   	var pathname = url.parse(req.url).pathname;
   	var n = pathname.lastIndexOf("/")+1;				 
	//获得api名字
	var api_name = pathname.substr(n);

	var method = req.method.toUpperCase()
	if (method == 'GET') {
		var params = url.parse(req.url, true).query;
		api(api_name,params,resp)
	}else {
		 var responseText=[];
		 req.addListener("data", function (data) {
             responseText.push(data) 
         });
		 req.addListener('end', function () {
		 	responseText = responseText.toString().replace(/\+/g, ' ')
		    p_list = responseText.split('&')
		    var params = new Array();
		    for (var i=0;i<p_list.length;i++){
				t_str = p_list[i]
				t_l = t_str.split('=')
				params[t_l[0]] = t_l[1]
			}
			api(api_name,params,resp)
    	});
	}
});

//监听8888接口
server.listen(8888);  

dlog('Server running at http://127.0.0.1:8888/');  

//调用api
api = function(api_name,params,resp) {
	var func = eval(api_name)
	func(params,resp)
}

//执行python
exec_python = function(file_path){
	 var script = 'python '+file_path
	 var arg_count = arguments.length
	 for (var i = 1; i < arg_count; i++) {
	 	script += ' '
	 	script += '"'+arguments[i]+'"'
	 };
	 exec(script,function (error, stdout, stderr) {
			if (error !== null) {
			    console.log('exec error: ' + error);
			}
	})
	return script
}

//约课
appoint_class = function(params,resp){
   	//直接调用命令
   	var script_path = '~/Desktop/IGS_Pro/documents/script/data.py'
   	var script = exec_python(script_path,params.cid)
   	resp.end('exec script is:' + script);  
}