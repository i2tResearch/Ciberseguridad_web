-- Create a file named by_ip/''ip_addess''.cap with all ip traffic of each ip host. (tshark only?)
-- Dump files are created for both source and destination hosts
function createDir (dirname)
    -- this will print out an error if the directory already exists, but that's fine
    os.execute("mkdir " .. dirname)
end

local dir = "by_ip"
createDir(dir)

-- create a table to hold the dumper objects/file handles
local dumpers = {}

-- create a listener tap.  By default it creates one for "frame", but we're tapping IP layer.
-- Valid values can be any protocol with tapping support, but to get something useful in the
-- "extractor" argument of the tap's 'packet' function callback (the third argument passed by
-- wireshark into it), it has to be one of the following currently: 
-- "actrace", "ansi_a", "ansi_map", "bacapp", "eth", "h225", "http", "ip", "ldap", 
-- "smb", "smb2", "tcp", "udp", "wlan", and "frame"
local tap = Listener.new("ip")


-- we will be called once for every IP Header.
-- If there's more than one IP header in a given packet we'll dump the packet once per every header
function tap.packet(pinfo,tvb,ip)
    --print("packet called")
    local ip_src, ip_dst = tostring(ip.ip_src), tostring(ip.ip_dst)
    local src_dmp, dst_dmp

    -- get the dumper file handle for this ip addr
    src_dmp = dumpers[ip_src]
    if not src_dmp then
        -- doesn't exist, make a new one, of the same encapsulation type as current file
        src_dmp = Dumper.new_for_current( dir .. "/" .. ip_src .. ".pcap" )
        dumpers[ip_src] = src_dmp
    end

    -- dump the current packet as it is (same encap format and content)
    src_dmp:dump_current()
    src_dmp:flush()

    -- now do the same for dest addr
    dst_dmp = dumpers[ip_dst]
    if not dst_dmp then
        dst_dmp = Dumper.new_for_current( dir .. "/" .. ip_dst .. ".pcap" )
        dumpers[ip_dst] = dst_dmp
    end

    dst_dmp:dump_current()
    dst_dmp:flush()

end

-- a listener tap's draw function is called every few seconds in the GUI
-- and at end of file (once) in tshark
function tap.draw()
    --print("draw called")
    for ip_addr,dumper in pairs(dumpers) do
             dumper:flush()
    end
end

-- a listener tap's reset function is called at the end of a live capture run,
-- when a file is opened, or closed.  Tshark never appears to call it.
function tap.reset()
    --print("reset called")
    for ip_addr,dumper in pairs(dumpers) do
             dumper:close()
    end
    dumpers = {}
end