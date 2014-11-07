(($) -> ) jQuery #jquery

$(document).ready ->  
  $.ajaxSetup beforeSend: (xhr, settings) ->
    getCookie = (name) ->
      cookieValue = null
      if document.cookie and document.cookie isnt ""
        cookies = document.cookie.split(";")
        i = 0
        while i < cookies.length
          cookie = jQuery.trim(cookies[i]) 
          # Does this cookie string begin with the name we want?
          if cookie.substring(0, name.length + 1) is (name + "=")
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
            break
          i++
      cookieValue

    # Only send the token to relative URLs i.e. locally.
    xhr.setRequestHeader "X-CSRFToken", getCookie("csrftoken")  unless /^http:.*/.test(settings.url) or /^https:.*/.test(settings.url)
    return


vote = (id, direction) ->
  console.log "#{id} - #{direction}"
  $.post "/post/" + id + "/" + direction + "vote/",
    HTTP_X_REQUESTED: "XMLHttpRequest"
  , ((data) ->
    if data.success is true 
     #console.log "ok-bunbun"
     $("#score").text(data.score.score)
     $("#total_votes").text(data.score.num_votes)
    else
      console.log "ERROR: " + data.error_message
    return
  ), "json"
  return
