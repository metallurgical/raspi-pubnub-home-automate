<script src="http://cdn.pubnub.com/pubnub-3.7.1.min.js"></script>

var pubnub = PUBNUB.init({
    publish_key: '<publish-key>',
    subscribe_key: '<scubscribe-key>'
});

var pubmsg = { 
  req : "toggle", 
  pin: "16" 
};

// Call this code when button click or whatever event you want
pubnub.publish({
    channel : '<pub-nub-channel>' ,
    message :  pubmsg
});
    
