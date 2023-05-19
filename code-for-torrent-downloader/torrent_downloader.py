# Import libtorrent module
import libtorrent as lt


# Function to download torrent
def download_torrent(torrent_file, save_path):
    ses = lt.session()
    params = {
        'save_path': save_path,
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error_occur': True
    }

    handle = ses.add_torrent(params, str(torrent_file))
    print('Downloading:', handle.name())

    while not handle.is_seed():
        s = handle.status()
        print('Progress: %.2f%%' % (s.progress * 100))
        print('Download Speed: %.2f kB/s' % (s.download_rate / 1000))
        print('Total Downloaded: %.2f MB' % (s.total_done / (1024 * 1024)))
        print('Peers:', s.num_peers)

        if s.progress == 1:
            break

    print('Hurry! Download complete!')


# Example for usage
torrent_file_path = 'path/to/your/torrent_file.torrent'
save_path = 'path/to/save/directory'
download_torrent(torrent_file_path, save_path)
