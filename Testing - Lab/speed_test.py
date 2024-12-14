import speedtest as st


test = st.Speedtest()

test.get_best_server()

download_speed = test.download() / 1_000_000
upload_speed = test.upload() / 1_000_000

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
