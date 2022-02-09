import requests
import json
from requests.api import get
from requests.models import HTTPBasicAuth, Response
from assertpy.assertpy import assert_that



"""
KapiTest will test the request of apis for your organization.
Testing CRUD api calls. 
"""


def Statcodes(statco):
  Result_Codes ={200: "Indicates that the request has succeeded.",
                   201: "Indicates that the request has succeeded and a new resource has been created as a result.",
                   202: "The request for processing was approved but the processing was not completed. Eventually, the request may be acted upon and may be disallowed when processing takes place. This is meant for cases where the requests are handled by another process or server, or for batch processing.",
                   203: "This status code simply means that the meta information returned is not exactly the same as the information available from the origin server, but is obtained from a copy of a local or a third party. That is mostly useful for other resource backups.",
                   204: "This status code shows where no content is sent for a particular request, although the headers may be useful. The user agent can update its cached headers with new ones for this resource.",
                   205: "This status code dictates that the user agent resets the document that sent the message.",
                   206: "This status code dictates that the user agent resets the document that sent the message.",
                   207: "This status code provides multiple , independent operations information. The message of the is an XML message by default and can provide different response codes, depending on how many sub-requests were made.",
                   208: "Used inside a response element to avoid repeated enumeration of multiple bindings to the same collection of internal members.",
                   226: "A GET request for the resource has been fulfilled by the server, and the answer is a representation of the outcome of one or more instance manipulations applied to the instance.",
                   301: "This HTTP response code indicates that the resource that is requested has permanently modified its unique URL. In the reply the new URL is given.",
                   302: "This code indicates that the resource requested was temporarily transferred to the URL. Future changes in the URL could also be made, so the same URL should be used in future requests. This is an example of industry practice that contradicts the norm.",
                   303: "When receiving this status code, it means that with a GET request, the server will send the response to direct the client to get the requested resource at another Address.",
                   304: "It means that a conditional request has been made by the client and access is allowed, but records have not been changed and the server should be responding with status code. It is necessary to remember that the answer 304 does not contain the body of the message, so that it is always terminated after the header fields by the first empty line.",
                   305: "This code is classified as an earlier version of the HTTP specification indicating that proxy access is needed to the requested response. It was deprecated because of security concerns regarding a proxy’s in and configuration.",
                   306: "The code is not used anymore. It used to mean that the specified proxy should be used with sub requests.",
                   307: "This means that the request should be replicated with another URI for that status code. Any future requests will still be using the initial URI, however. It is exactly like the 302 Found HTTP application, but with the exception that the user agent does not have to modify the form used for HTTP. If a POST was used in the first submission, the second request must have a POST used.",
                   308: "This status code means that the resource is not stored permanently on another URL. The Location must define this: HTTP Response Header. It is just like the 301 permanently moved response code, with the exception that the user agent does not alter the form used for HTTP. If a POST was used in the first submission, the second request must have a POST used.",
                   400: "400 is the generic error status on the client side, used when no other 4xx error code is suitable. Errors can be such as malformed request grammar, invalid request message parameters, or tricky request routing etc.The client DO NOT repeat the request unchanged.",
                   401: "A answer to a 401 error suggests that the client has attempted to work on a protected resource without providing the necessary authorisation. It could have given the wrong credentials, or none at all. The response must include a WWW-Authenticate header field which contains a challenge that is applicable to the resource requested.The client MAY repeat the request with an appropriate header Authorization field. If Authorization credentials have already been included in the submission, then the 401 response suggests that those credentials have been denied authorisation. If the 401 response contains the same challenge as the previous response, and the user agent has already attempted authentication at least once, then the user SHOULD will be faced with the entity provided in the response as that entity the contain relevant diagnostic data.",
                   402: "This answer code is for future use only. The initial objective was to use it for digital payment systems; however, the code is rarely used, and there is no standard for it.",
                   403: "A 403 error response indicates that the client request is correctly formed, but the REST API refuses to honor it, i.e. the user does not have the resource permissions. A 403 response is not a case of inadequate customer credentials; that would be 401 (‘Unauthorized’).Authentication won’t help, and DO NOT repeat the request. Unlike a 401 Unauthorized response, authenticating won’t make any difference.",
                   404: "The 404 error status code shows that the REST API is unable to map the Url of the client to a resource but may be available for potential use. Subsequent customer requests are admissible.No indication is given as to whether the condition is permanent or temporary. The 410 (Gone) status code SHOULD will be used if the server knows that an old resource is permanently unavailable and has no forwarding address, through some internally configurable mechanism. This status code is typically used when the server does not want to disclose precisely why the request was rejected, or when there is no other answer to it.",
                   405: "The API responds with an error of 405 indicating that the client has attempted to use an HTTP method which the tool does not allow. For example, a read-only resource could only support GET and HEAD, whereas a controller resource could allow GET and POST but not PUT or DELETE.A 405 answer must include the Allow header which lists the resource-supporting HTTP methods. For instance:Permit: GET, POST",
                   406: "The 406 error response indicates that, as indicated by the Accept request header, the API is not able to produce any of the desired media types on the device. For example, if the API is only willing to format data as application / json, a client request for data formatted as application / xml will receive a response of 406.If the response may be inappropriate, a user agent Must temporarily stops collecting further data and asks the user for more action decisions.",
                   407: "This response code is very similar to the 401 code, but proxy authentication is required.",
                   408: "This response is normally sent via the idle link of some server, often without the client making any previous request. When web browsers such as Chrome and Firefox use HTTP link mechanisms to speed up browsing, this basically means the server wants to close the idle link and the response is being used much more these days. Notice also that some servers can terminate the connection without issuing this notice.",
                   409: "This response he sent to the server when a request conflicts with the server’s current state.",
                   410: "This error notes that the requested resource is no longer available and will not be available again. This code should be used if a resource has been deleted deliberately, and the resource should not be purged. Upon obtaining a 410 status code, the customer will not request this tool again in the future. Clients like search engines can have the tool eliminated.",
                   411: "This response simply means the request did not indicate a connection to the content needed by the resource requested.",
                   412: "The 412 error response shows that in its request headers, the client specified one or more preconditions, essentially informing the REST API to execute its request only if those requirements have been met. A response from 412 indicates that certain requirements have not been met, so instead of executing the request, the API sends the status code.",
                   413: "Demand entity is larger than server-defined limits; the server may either close the connection or return a Retry-After header field.",
                   414: "The request is bigger than that which the server is willing or able to handle. Previously named “Too Big Software Unit”",
                   415: "The response to the 415 error indicates that the API is unable to process the type of media supplied by the client, as indicated by the request header Content-Type. For example, if the API is only willing to process data formatted as the application / json, a client request including data formatted as application / xml will receive a 415 response.The client uploads an image, for example, as image / svg+xml, but the server demands that images use a different format.The server refuses to process the request because the user entity is for the requested method in a format not accepted by the requested resource.",
                   416: "The range defined in the request by the Scope header field can not be fulfilled; it is possible the scope is outside the size of the data of the target URI.",
                   417: "The server can not fulfill the request-header requirements of the Expect sector.",
                   418: "The server refuses the attempt to brew a teapot with the coffee. In 1998, that code was defined as one of the traditional jokes of the IETF April Fools.",
                   421: "The request was addressed to a server which can not produce a response. It may be submitted by a server that is not designed to deliver responses that are included in the request URI for the combination of scheme and authority.",
                   422: "The request was well-formed but due to semantum errors could not be followed. For example, this condition of error may occur if there are well-formed (i.e., syntactically correct) but semantically erroneous XML instructions in the body of a request.",
                   423: "Access to the resource is locked.",
                   424: "The request failed as it was based on another request and failed.",
                   425: "Specifies that the server is not prepared to risk losing a request that could be replayed.",
                   426: "The server refuses to use the current protocol to execute the request but may be able to do so after the client switches to another protocol. In a 426 response, the server sends an Upgrade header indicating the protocol(s) required.",
                   428: "The server of origin requires conditionality to the submission. Intended to avoid the ‘lost update’ problem where a client GETs the state of a resource, modifies it, and PUTs it back to the server when a third party has changed the state on the server meanwhile leading to a conflict.",
                   429: "The 429 status code indicates that, within a given period of time, the user has submitted too many requests (“rate limit”). SHOULD ‘s response representations provide information describing the situation, and MAY contains a Retry-After header indicating how long to wait before creating a new submission. If a server is under attack or simply receives a very large number of requests from a single user, it will consume resources to respond to each with a 429 status code.",
                   431: "The 431 status code indicates that since its header fields are too large, the server is reluctant to process the request. The request Will will be resubmitted after the code header fields are reduced in size. This can be used both when the total collection of request header fields is too wide, and when the fault of a single header field. In the latter case, which header area was too wide should be defined by the answer representation.",
                   451: "The user-agent asked for a tool that can not be legally given, such as a government-censored website",
                   500: "A generic error message, given when an unexpected condition was encountered and no more specific message is suitable",
                   501: "The server either does not recognize the request method, or it lacks the ability to fulfil the request. Usually this implies future availability (e.g., a new feature of a web-service API)",
                   502: "The server was acting as a gateway or proxy and received an invalid response from the upstream server",
                   503: "The server cannot handle the request (because it is overloaded or down for maintenance). Generally, this is a temporary state",
                   504: "The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.",
                   505: "The server does not support the HTTP protocol version used in the request.",
                   506: "Transparent content negotiation for the request results in a circular reference.",
                   507: "The server is unable to store the representation needed to complete the request.",
                   508: "The server detected an infinite loop while processing the request (sent instead of 208 Already Reported).", 
                   510: "Further extensions to the request are required for the server to fulfil it", 
                   511: "The client needs to authenticate to gain network access. Intended for use by intercepting proxies used to control access to the network (e.g., captive portals used to require agreement to Terms of Service before granting full Internet access via a Wi-Fi hotspot).[57]"
                   }
  return print(Result_Codes.get(statco))

def Api_Headers(site):
    response = requests.get(site)
    x = response.headers
    Statcodes(x)
 


def Status_Response_Code(site):
    response = requests.get(site)
    x = json.loads(response.text)
    print(response)
    formater = json.dumps(x, indent=15)
    print(formater)
Status_Response_Code("https://api.github.com/")


def Validate_Status_Code(site):
    result = requests.get(site)
    Reqs = result.status_code
    print(Reqs)
    Statcodes(Reqs)


def Api_Post(api, key, value):
   resp = requests.post(api, data={key:value})
   #print(Result_Codes.get(resp))
   Statcodes(resp)
 
def Api_Put(api, key, value):
   resp = requests.put(api, data={key:value})
   #print(Result_Codes.get(resp))
   Statcodes(resp)

#This will post a delete api call print what king of result it maybe  
def Api_Delete(api):
   resp = requests.delete(api)
   Statcodes(resp)



def Api_Get_Auth(api, username, password, key, value):  
  x = requests.get(api, auth=HTTPBasicAuth(username, password), data= {key:value})
  #print(Result_Codes.get(x)) 
  Statcodes(x)  
             
def Api_Delete_Auth(api, username, password, key, value):  
  x = requests.delete(api, auth=HTTPBasicAuth(username, password), data= {key:value})
  #print(Result_Codes.get(x)) 
  Statcodes(x)
      

def Api_Post_Auth(api, username, password, key, value):  
  x = requests.post(api, auth=HTTPBasicAuth(username, password), data= {key:value})
  Statcodes(x)

