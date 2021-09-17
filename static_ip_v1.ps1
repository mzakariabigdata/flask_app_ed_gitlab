$windowsIp = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias Wi-Fi).IPAddress
$wslIp = bash -c "ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"

Write-Output "Show v4tov4 port forwards ..."
Invoke-Expression "netsh interface portproxy show v4tov4"

Write-Output "Remove all portproxy"
Invoke-Expression "netsh int portproxy reset all"

Write-Output "Remove Firewall Exception Rules"
(Invoke-Expression "Remove-NetFireWallRule -DisplayName '_WSL 2 Firewall Unlock' ") *>&1;

# [Ports]
Write-Output "All the ports you want to forward separated by coma..."
$ports = @(
    9000
);
$ports_a = $ports -join ",";
Write-Output $ports_a
Write-Output ""

Write-Output "Adding Exception Rules for inbound and outbound Rules..."
(Invoke-Expression "New-NetFireWallRule -DisplayName '_WSL 2 Firewall Unlock' -Direction Outbound -LocalPort $ports_a -Action Allow -Protocol TCP").Name *>&1;
(Invoke-Expression "New-NetFireWallRule -DisplayName '_WSL 2 Firewall Unlock' -Direction Inbound -LocalPort $ports_a -Action Allow -Protocol TCP").Name *>&1;
Write-Output ""

for ( $i = 0; $i -lt $ports.length; $i++ ) {
   $port = $ports[$i];
   $command = "netsh interface portproxy add v4tov4 listenport=$port listenaddress=172.26.234.41 connectport=$port connectaddress=172.28.114.195"
   Write-Output "Running: $command"
   Invoke-Expression $command;
}